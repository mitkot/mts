"""Database setup and session utilities."""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings


class Base(DeclarativeBase):
    """Base model for SQLAlchemy models."""


engine = create_engine(settings.database_url, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


def init_db() -> None:
    """Create all tables (minimal bootstrap approach)."""
    from app import models  # noqa: F401

    Base.metadata.create_all(bind=engine)
