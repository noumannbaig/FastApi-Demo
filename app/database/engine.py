from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.engine import url

"""Database engine."""
from config import (
    DB_DRIVER,
    DB_HOST,
    DB_NAME,
    DB_PASS,
    DB_PORT,
    DB_SSLMODE,
    DB_USER,
)
db_url = url.URL.create(
    DB_DRIVER,
    host=DB_HOST,
    port=DB_PORT,
    username=DB_USER,
    password=DB_PASS,
    database=DB_NAME,
)
# DATABASE_URL = "postgresql://postgres:"+ f"{password}" + "@localhost/users"
connect_args = {}

if DB_DRIVER == "postgresql+psycopg2":
    connect_args["sslmode"] = DB_SSLMODE
engine = create_engine(db_url,
    echo = True
)

