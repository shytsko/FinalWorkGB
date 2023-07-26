import uuid
from enum import Enum

from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from db.session import Base


class UserRole(str, Enum):
    ROLE_USER = "ROLE_USER"
    ROLE_ADMIN = "ROLE_PORTAL_ADMIN"
    ROLE_SUPERADMIN = "ROLE_SUPERADMIN"


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True)
    hashed_password = Column(String, nullable=False)
    roles = Column(ARRAY(String), nullable=False)
