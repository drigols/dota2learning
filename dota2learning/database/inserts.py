# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy.engine.reflection import Inspector

from dota2learning.database.connection import Connection


def insert_into_table(model, data):

    # Database Connection.
    connEngine = Connection().get_engine_connection()

    # Check if table exists.
    if Inspector(connEngine).has_table(model.__tablename__):
        try:
            connEngine.execute(model.__table__.insert(data))
            print("Data inserted successfully!")
        except Exception as error:
            print("My error:", error)
    else:
        print("Error to insert data!")
