from pydantic import BaseModel
from typing import Optional

class SeashellBase(BaseModel):
    name: str
    species: str
    description: Optional[str] = None
    origin: Optional[str] = None
    color: Optional[str] = None 

class SeashellCreate(SeashellBase):
    pass

class SeashellResponse(SeashellCreate):
    id: int

    class Config:
        from_attributes = True

class Message(BaseModel):
    message: str
    
