from typing import List

from pydantic import BaseModel


class LocationBase(BaseModel):
	key: str
	place_name: str = None
	city: str
	latitude: float
	longitude: float


class LocationCreate(LocationBase):
	pass

class Location(LocationBase):
	key: str

	class Config:
		orm_mode = True