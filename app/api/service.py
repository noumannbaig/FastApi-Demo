from sqlalchemy.orm import Session
import uuid
from datetime import datetime, timezone
from api.db_models import User
from api.api_models import UserBase,UserCreate
from database.session import update_session 

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    meta_dict = dict(
        create_time=datetime.now(timezone.utc),
        update_time=datetime.now(timezone.utc),
    )
    db_user = User(id=uuid.uuid4(),
                   email=user.email, 
                   hashed_password=fake_hashed_password,
                   **meta_dict
                   )
    update_session(db_user,session=db)
    return db_user


