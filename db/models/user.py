from . import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"

    login: Mapped[int]
    password: Mapped[str] = mapped_column(nullable=False)