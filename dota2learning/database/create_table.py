# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy.engine.reflection import Inspector

from dota2learning.database.connection import get_engine_connection
from dota2learning.database.settings import db_settings


def create_table_if_not_exists(model):

    # Database Connection.
    connEngine = get_engine_connection(**db_settings)

    # Check if table exists.
    if not Inspector(connEngine).has_table(model.__tablename__):
        model.metadata.create_all(connEngine)
        print("Table created successfully!")
    else:
        print("Your table already exists!")
