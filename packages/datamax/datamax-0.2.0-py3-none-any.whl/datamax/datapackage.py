from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from typing import List, Optional
import pathlib

class ResourceField(BaseModel):
    name: str
    type: str
    description: Optional[str] = None
    format: Optional[str] = None
    constraints: Optional[dict] = None


class ResourceSchema(BaseModel):
    fields: List[ResourceField]

class Resource(BaseModel):
    path: pathlib.Path
    resource_schema: Optional[ResourceSchema] = Field(alias="schema")

class Source(BaseModel):
    model_config = ConfigDict(
            alias_generator=to_camel
        )
    name: str
    data_published_by: Optional[str] = None
    data_publisher_source: Optional[str] = None
    link: str
    retrieved_date: Optional[str] = None
    additional_info: Optional[str] = None

class DataPackage(BaseModel):
    description: str
    resources: List[Resource] = []
    sources: List[Source] = []
    collection: Optional[str] = None
    name: str
    keywords: List[str] = []
