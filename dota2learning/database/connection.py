# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

import sys

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.pool import NullPool


def get_engine_connection(
    username: str,
    password: str,
    database: str,
    host: str = "localhost",
    port: int = 3306,
):
    """Function to get an Enginer connection reference.

    Args:
        username (str): Database username to connect.
        password (str): Password for your username connection.
        database (str): Database name you want to connect.
        host (str, optional): Hostname. Defaults to "localhost".
        port (int, optional): Service port. Defaults to "3306".

    Returns:
        <class 'sqlalchemy.engine.base.Connection'>:
        The return is an Engine connection reference to the Database.
    """
    try:
        engine = create_engine(
            f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}",
            echo=False,
            poolclass=NullPool,
        )
        connection = engine.connect()
    except OperationalError:
        print("OperationalError: Check your dialect URL or database service.")
        sys.exit()
    else:
        connection.close()
        return engine
