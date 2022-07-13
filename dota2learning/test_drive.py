# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from dota2learning.database.connection import Connection
from dota2learning.database.create_table import create_table_if_not_exists
from dota2learning.models.hero_model import HeroModel


if __name__ == "__main__":

    # Connection instance.
    db = Connection()

    # Connection Testing.
    connEngine = db.get_engine_connection()
    print("\nConnection Testing:")
    print("Variable result:", connEngine)
    print("Type Result:", type(connEngine))
    print("Bool result:", bool(connEngine))

    # Session Testing.
    print("\nSession Testing:")
    sess = db.get_session()
    print("Variable result:", sess)
    print("Type Result:", type(sess))
    print("Bool result:", bool(sess))

    # Create Table Testing.
    print("\nCreate Table Testing:")
    cTable = create_table_if_not_exists(model=HeroModel)
    print("Variable result:", cTable)
    print("Type Result:", type(cTable))
    print("Bool result:", bool(cTable))
