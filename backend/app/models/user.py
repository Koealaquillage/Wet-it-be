from pydantic import BaseModel

class User(BaseModel):
    name: str
    phone: str
    crop_type: str
    location: str
