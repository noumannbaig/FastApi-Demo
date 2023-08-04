
import uuid
import re
from pydantic import BaseModel, validator, constr
from datetime import datetime
from enum import Enum
from typing import List, Optional

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True