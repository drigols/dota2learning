# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy import insert
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy.exc import IntegrityError

from dota2learning.database.connections import get_engine_connection
from dota2learning.settings import db_settings


def insert_data_into_table(model, data):
    """Function to insert data into an existing table.

    Args:
        model: SQLAlchemy table model.
        data: Data to insert into table.
    """

    # Get table name from SQLAlchemy model.
    table = model.__tablename__

    # Get Engine connection.
    engine = get_engine_connection(**db_settings)

    try:
        if not Inspector(engine).has_table(table):
            print(f'Table "{table}" no exists.')
        else:
            # Create insert mapping (model > data).
            insertQueryMapping = insert(model).values(data)
            with engine.begin() as connection:
                connection.execute(insertQueryMapping)
                print(f'Data inserted into table "{table}" successfully!')
    except IntegrityError:
        print("IntegrityError: You probably already have that record.")
