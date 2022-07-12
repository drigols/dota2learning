# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connection:

    user: str = "root"
    passwd: str = "toor"
    host: str = "localhost"
    dbName: str = "dota2learning-db"
    port: str = "3306"
    DATABASE_URL = f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{dbName}"

    def __init__(self) -> None:
        self.connection_is_active = False
        self.engine = None

    def get_engine_connection(self):
        if self.connection_is_active is False:
            try:
                self.engine = create_engine(
                    self.DATABASE_URL,
                )
                return self.engine
            except Exception as error:
                print(error)
        return self.engine

    def get_session(self, engine):
        try:
            Session = sessionmaker(
                autocommit=False, autoflush=False, bind=engine
            )
            session = Session()
            return session
        except Exception as error:
            print(error)
            return None
