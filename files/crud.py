from sqlalchemy.orm import Session

from . import models, schemas


"""def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
"""

def get_location_by_ll(db: Session, latitude: float, longitude:float):
	return db.query(models.Location).filter(models.Location.latitude == latitude and models.Location.longitude == longitude).first()


def add_location(db: Session, loc: schemas.LocationCreate):
	db_data = models.Location(latitude=loc.latitude, longitude = loc.longitude, place_name = loc.place_name, city = loc.city, key = loc.key)
	db.add(db_data)
	db.commit()
	db.refresh(db_data)
	return db_data

"""
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
"""