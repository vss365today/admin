from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import BigInteger, DateTime, String

db = SQLAlchemy()


__all__ = ["User"]

class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {"comment": "Store the #vss365 admin users."}

    _id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(
        String(32, collation="utf8mb4_unicode_ci"), unique=True
    )
    password: Mapped[str] = mapped_column(
        String(256, collation="utf8mb4_unicode_ci"), nullable=False
    )
    date_created: Mapped[datetime] = Column(
        DateTime,
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now,
    )
    date_last_login: Mapped[datetime] = Column(
        DateTime,
        nullable=True,
        default=None
    )
    api_token: Mapped[str] = mapped_column(
        String(256, collation="utf8mb4_unicode_ci"), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
