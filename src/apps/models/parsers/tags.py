from pydantic import BaseModel, Field


class TagOR(BaseModel):
    content: str
    property_name: str
    source: str

