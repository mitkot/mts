"""Database setup and session utilities.

Compatible with SQLAlchemy 1.4 and 2.x.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

try:  # SQLAlchemy 2.x
    from sqlalchemy.orm import DeclarativeBase

    class Base(DeclarativeBase):
        """Base model for SQLAlchemy models."""

except ImportError:  # SQLAlchemy 1.4 fallback
    from sqlalchemy.orm import declarative_base

    Base = declarative_base()


engine = create_engine(settings.database_url, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


def init_db() -> None:
    """Create all tables (minimal bootstrap approach)."""
    from app import models  # noqa: F401

    Base.metadata.create_all(bind=engine)
