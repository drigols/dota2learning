# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Database settings.
username: str = "root"
password: str = "toor"
hostname: str = "localhost"
database: str = "dota2learning-db"

DATABASE_URL = f"mysql+pymysql://{username}:{password}@{hostname}/{database}"

# Database Connection (engine)
engine = create_engine(
    DATABASE_URL,
    echo=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
