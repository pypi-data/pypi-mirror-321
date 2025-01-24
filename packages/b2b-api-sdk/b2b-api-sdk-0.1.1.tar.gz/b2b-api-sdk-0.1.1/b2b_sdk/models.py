from pydantic import BaseModel

class Resource(BaseModel):
    id: str
    name: str
    status: str
