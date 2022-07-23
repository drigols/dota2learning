# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from dota2learning.database.connection import get_engine_connection
from dota2learning.settings import db_settings


if __name__ == "__main__":

    # Testing connection.
    engine = get_engine_connection(
        username="root",
        password="toor",
        database="dota2learning-db",
        host="localhost",
        port=3306,
    )
    print("Testing connection:")
    print("Variable result:", engine)
    print("Type Result:", type(engine))
    print("Bool result:", bool(engine))
