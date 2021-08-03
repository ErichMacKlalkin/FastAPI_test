from pydantic import BaseModel
from typing import Optional
import datetime


class EntityIn(BaseModel):
    name: Optional[str]
    date: Optional[datetime.date]
    content: Optional[str]
    owner: Optional[str]


class Entity(BaseModel):
    id: int
    name: str
    date: datetime.date
    content: str
    owner: str


class EntityInPartial(BaseModel):
    name: Optional[str]
    date: Optional[datetime.date]
    content: Optional[str]
    owner: Optional[str]