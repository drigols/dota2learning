# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from dota2learning.api.opendota import get_heroes_stats
from dota2learning.database.connections import get_engine_connection
from dota2learning.database.create_tables import create_table_if_not_exists
from dota2learning.database.inserts import insert_data_into_table
from dota2learning.models.hero_model import fakeHeroInsert
from dota2learning.models.hero_model import HeroModel
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
    print("\nTesting connection:")
    print("Returned value:", engine)
    print("Returned value type:", type(engine))

    # Testing create table if not exists.
    print("\nTesting create table if not exists:")
    ctifnoexResult = create_table_if_not_exists(HeroModel)
    print("Returned value:", ctifnoexResult)
    print("Returned value type:", type(ctifnoexResult))

    # Testing insert data into table.
    print("\nTesting insert data into table:")
    insertResult = insert_data_into_table(HeroModel, get_heroes_stats())
    print("Returned value:", insertResult)
    print("Returned value type:", type(insertResult))
    # insert_data_into_table(HeroModel, fakeHeroInsert)
