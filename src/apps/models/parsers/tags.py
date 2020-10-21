from pydantic import BaseModel


class TagOR(BaseModel):
    content: str
    property_name: str
    source: str
