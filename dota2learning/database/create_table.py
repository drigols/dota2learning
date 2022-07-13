# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy.engine.reflection import Inspector

from dota2learning.database.connection import Connection


def create_table_if_not_exists(model):

    # Database Connection.
    connEngine = Connection().get_engine_connection()

    # Check if table exists.
    if not Inspector(connEngine).has_table(model.__tablename__):
        model.metadata.create_all(connEngine)
        print("Table created successfully!")
    else:
        print("Your table already exists!")
