"""Setup for base model and database connection used by all defined api_models.
"""
import uuid

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TableBase:
    """Base model which defines common attributes that
    should be inherited by all database api_models."""

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    create_time = Column(DateTime(timezone=True), nullable=False)
    update_time = Column(DateTime(timezone=True), nullable=False)