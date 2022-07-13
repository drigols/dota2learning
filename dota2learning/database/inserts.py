# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy.engine.reflection import Inspector

from dota2learning.database.connection import get_engine_connection
from dota2learning.database.settings import db_settings


def insert_into_table(model, data):

    # Database Connection.
    connEngine = get_engine_connection(**db_settings)

    # Check if table exists.
    if Inspector(connEngine).has_table(model.__tablename__):
        try:
            connEngine.execute(model.__table__.insert(data))
            print("Data inserted successfully!")
        except Exception as error:
            print("My error:", error)
    else:
        print("Error to insert data!")
