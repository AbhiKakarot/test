from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Location(Base):

	__tablename__ = "location_data"
	key = Column(String, primary_key=True)
	place_name = Column(String)
	city = Column(String)
	latitude = Column(Float)
	longitude = Column(Float)
	