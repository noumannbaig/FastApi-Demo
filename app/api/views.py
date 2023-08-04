from fastapi import FastAPI,HTTPException,APIRouter,Depends,Body

from api.api_models import User,UserCreate
from api.service import create_user,get_user_by_email
from sqlalchemy.orm import Session
from database.session import get_db
user_router = APIRouter()


@user_router.get("/")
async def root():
    return {"message": "hello world"}


@user_router.post("/users",response_model=User)
def add_user(db: Session = Depends(get_db),
                user:UserCreate=Body(...)
):
    users=get_user_by_email(db,email=user.email)
    if users:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db = db, user=user)