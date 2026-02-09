from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Seashell(Base):
    __tablename__ = "seashells"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    species = Column(String)
    description = Column(Text)
    origin = Column(String)
    color = Column(String)
