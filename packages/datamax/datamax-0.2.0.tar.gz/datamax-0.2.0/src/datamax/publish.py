import pathlib
from datamax.console import tty
from datamax.datapackage import DataPackage, Resource
from datamax.client import DatamaxClient
from pyarrow import csv, parquet, Table # type: ignore
from tempfile import TemporaryDirectory
import shutil
import requests
from functools import partial
from multiprocessing import Pool
import re

class Publisher:

    def __init__(self, publish_username: str, path: pathlib.Path, api_host: str):
        self.publish_username = publish_username
        self.base_path = path
        self.client = DatamaxClient(api_host)
    
    def _sanitize_name(self, name: str, preserve_extension: bool = False) -> str:
        """Convert name to BigQuery-safe format.
        - Lower-case all characters
        - Replace any non-alphanumeric characters (including commas) with underscore
        - Remove consecutive underscores
        - Optionally preserve file extension
        """
        if preserve_extension:
            # Split into base name and extension(s)
            path = pathlib.Path(name)
            base = path.stem
            extension = ''.join(path.suffixes)
            
            # Sanitize only the base name
            safe_base = re.sub(r'[^a-zA-Z0-9_]', '_', base.lower())
            safe_base = re.sub(r'_+', '_', safe_base)
            safe_base = safe_base.rstrip('_')
            
            # Recombine with extension
            return safe_base + extension
        else:
            # Original behavior for non-filenames
            safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', name.lower())
            safe_name = re.sub(r'_+', '_', safe_name)
            safe_name = safe_name.rstrip('_')
            return safe_name

    def _parse_datapackage_json(self, temp_dir: pathlib.Path):
        datapackage_path = self.base_path / "datapackage.json"
        tty.log(f"parsing {datapackage_path}")
        with open(datapackage_path, "r") as f:
            package = DataPackage.model_validate_json(f.read())
        # Sanitize dataset name (no extension preservation needed for dataset name)
        package.name = self._sanitize_name(package.name, preserve_extension=False)
        
        # First copy all files to temp dir
        for resource in package.resources:
            shutil.copy2(self.base_path / resource.path, temp_dir / resource.path)
        
        # Process each resource
        for resource in package.resources:
            # Sanitize the file name and update the path
            old_path = resource.path
            # Preserve extension for both the file copy and the path in datapackage.json
            sanitized_path = self._sanitize_name(str(old_path), preserve_extension=True)
            new_path = pathlib.Path(sanitized_path)
            if old_path != new_path:
                tty.log(f"Renaming {old_path} to {new_path}")
                # Rename the file in the temp directory
                (temp_dir / old_path).rename(temp_dir / new_path)
                # Update the resource path
                resource.path = new_path
            
            # Convert to parquet (this will further sanitize column names)
            self.convert_to_parquet(temp_dir, resource)
        
        # Write updated datapackage.json to temp dir
        with open(temp_dir / "datapackage.json", "w") as f:
            f.write(package.model_dump_json())
        
        return package

    def publish(self):
        tty.log(f"Publishing from {self.base_path} as {self.publish_username}...")
        with TemporaryDirectory() as temp_dir:
            temp_dir_path = pathlib.Path(temp_dir)
            tty.log(f"Using temp dir {temp_dir}")
            data_package = self._parse_datapackage_json(temp_dir_path)
            with open(temp_dir_path / "datapackage.json", "w") as f:
                f.write(data_package.model_dump_json())
            if len([readme := r.name for r in self.base_path.iterdir() if r.name.lower() in ["readme.md", "readme"]]) > 0:
                shutil.copyfile(self.base_path / readme, temp_dir_path / readme) # type: ignore
            dataset_id = self.push_dataset(data_package, temp_dir_path)
            tty.log(f"Dataset {dataset_id} published")

    def push_dataset(self, data_package: DataPackage, temp_dir: pathlib.Path):
        tty.print("Pushing dataset to substrate...")
        maybe_readme = [r.name for r in temp_dir.iterdir() if r.name.lower() in ["readme.md", "readme"]]
        if len(maybe_readme) > 0:
            with open(temp_dir / maybe_readme[0], "r") as f:
                readme = f.read()
        else:
            readme = None
        presigned_urls = self.client.publish(data_package, {"name": maybe_readme[0], "content": readme})
        dataset_id = presigned_urls["datasetId"]
        local_curry = partial(self.handle_presigned_url, temp_dir, dataset_id)
        upload_res = Pool().map_async(local_curry, presigned_urls["urls"], error_callback=tty.log)
        upload_res.wait(120)
        if not upload_res.successful():
            tty.log("Failed to upload all resources")
            raise Exception("Failed to upload all resources")
        
        # Check for non-empty string responses
        upload_results = upload_res.get()
        non_empty_responses = [i for i, res in enumerate(upload_results) if res]
        if non_empty_responses:
            tty.log(f"Warning: Non-empty responses received for uploads at indices: {non_empty_responses}")
            
        tty.log("Successfully uploaded all resources")
        process_res = self.client.process(dataset_id)
        if not process_res.ok:
            tty.log("Failed to process dataset")
            raise Exception("Failed to process dataset")
        return dataset_id

    def handle_presigned_url(self, temp_dir: pathlib.Path, dataset_id: str, resource: dict[str, str]):
        url = resource["url"]
        file_name = resource["file"]
        return requests.put(url, data=open(temp_dir / file_name, "rb")).text

    def convert_to_parquet(self, temp_dir: pathlib.Path, resource: Resource):
        tty.print(f"Converting {resource.path} to parquet...")
        extension = ".".join(resource.path.suffixes)
        match extension:
            case ".csv":
                self._convert_csv_to_parquet(temp_dir, resource)
            case ".parquet":
                self._sanitize_parquet(temp_dir, resource)
            # case ".json":
            #     self._convert_json_to_parquet(resource)
            case _:
                tty.log(f"Unsupported file type: {extension}")

    def _sanitize_parquet(self, temp_dir: pathlib.Path, resource: Resource):
        # Read the parquet file from temp dir
        table = parquet.read_table(temp_dir / resource.path)
        
        # Create a mapping of original to sanitized names
        name_mapping = {name: self._sanitize_name(name) for name in table.column_names}
        
        # Rename columns in the table
        table = Table.from_arrays(
            table.columns,
            names=[name_mapping[name] for name in table.column_names]
        )
        
        # Update the schema in the resource to match the new column names
        if resource.resource_schema and resource.resource_schema.fields:
            for field in resource.resource_schema.fields:
                if field.name in name_mapping:
                    field.name = name_mapping[field.name]
        
        # Save as parquet in temp dir
        parquet.write_table(table, temp_dir / resource.path, flavor="spark")

    def _convert_csv_to_parquet(self, temp_dir: pathlib.Path, resource: Resource):
        # Read the CSV from temp dir
        table = csv.read_csv(temp_dir / resource.path)
        
        # Create a mapping of original to sanitized names
        name_mapping = {name: self._sanitize_name(name) for name in table.column_names}
        
        # Rename columns in the table
        table = Table.from_arrays(
            table.columns,
            names=[name_mapping[name] for name in table.column_names]
        )
        
        # Update the schema in the resource to match the new column names
        if resource.resource_schema and resource.resource_schema.fields:
            for field in resource.resource_schema.fields:
                if field.name in name_mapping:
                    field.name = name_mapping[field.name]
        
        # Save as parquet in temp dir
        new_path = resource.path.with_suffix(".parquet")
        resource.path = new_path
        parquet.write_table(table, temp_dir / new_path, flavor="spark")
