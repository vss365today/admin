from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Integer, DateTime, String

db = SQLAlchemy()


__all__ = ["User", "db"]


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {
        "comment": "Store the #vss365 admin users.",
        "sqlite_autoincrement": True,
    }

    _id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    password: Mapped[str] = mapped_column(String(256), nullable=False)
    date_created: Mapped[datetime] = Column(
        DateTime,
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now,
    )
    date_last_login: Mapped[datetime] = Column(DateTime, nullable=True, default=None)
    api_token: Mapped[str] = mapped_column(String(256), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
