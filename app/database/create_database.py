from app.database import engine
from app.database.core import Base
from sqlalchemy.ext.declarative import declarative_base
print("Creating database...")

Base.metadata.create_all(engine)