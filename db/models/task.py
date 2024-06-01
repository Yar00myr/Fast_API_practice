from . import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped


class Task(Base):
    __tablename__ = "task"

    creator: Mapped[str]
    title: Mapped[str]
    content: Mapped[str]