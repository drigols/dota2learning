# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy.engine.reflection import Inspector

from dota2learning.database.connection import get_engine_connection
from dota2learning.settings import db_settings


def create_table_if_not_exists(model):
    """Function to create table if not exists in the Database.

    Args:
        model (object):
            The argument received is an SQLAlchemy table (base model).
    """

    # Get Engine connection.
    engine = get_engine_connection(**db_settings)

    try:
        # Check if table exists.
        if Inspector(engine).has_table(model.__tablename__):
            print(f'Table "{model.__tablename__}" already exists!')
        else:
            model.metadata.create_all(engine)
            print(f'Table "{model.__tablename__}" created successfully!')
    except Exception as error:
        print(error)
