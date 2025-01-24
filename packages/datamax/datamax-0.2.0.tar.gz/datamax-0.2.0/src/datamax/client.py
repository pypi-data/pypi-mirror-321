from datamax.console import tty
from datamax.datapackage import DataPackage
import requests
from typing import Optional, Dict, List, TypedDict
import os

class PublishResponse(TypedDict):
    urls: List[Dict[str, str]]
    datasetId: str

class DatamaxClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.api_key = os.environ.get("DATAMAX_API_KEY")

    @property
    def publish_url(self):
        return f"{self.base_url}/api/v1/publish"
    
    def process_url(self, dataset_id: str):
        return f"{self.base_url}/api/v1/dataset/{dataset_id}/process"

    def publish(self, data_package: DataPackage, readme: Optional[Dict[str, list[str] | str | None]] = None, user_id: Optional[str] = None) -> PublishResponse:
        tty.print(f"Publishing to {self.publish_url}")
        user_id = user_id or os.environ.get("DATAMAX_USER_ID")
        if not self.api_key:
            raise ValueError("DATAMAX_API_KEY environment variable is not set")
        headers = {
            "x-user-id": user_id,
            "x-api-key": self.api_key
        }
        res = requests.post(self.publish_url, json={"dataPackage": data_package.model_dump_json(by_alias=True), "readme": readme}, headers=headers)
        return res.json()

    def process(self, dataset_id: str):
        if not self.api_key:
            raise ValueError("DATAMAX_API_KEY environment variable is not set")
        headers = {"x-api-key": self.api_key}
        res = requests.post(self.process_url(dataset_id), headers=headers)
        return res
