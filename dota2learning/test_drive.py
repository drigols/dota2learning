# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from dota2learning.database.connection import get_engine_connection
from dota2learning.database.create_table import create_table_if_not_exists
from dota2learning.models.hero_model import HeroModel
from dota2learning.settings import db_settings


if __name__ == "__main__":

    # Testing connection.
    # engine = get_engine_connection(
    #    username="root",
    #    password="toor",
    #    database="dota2learning-db",
    #    host="localhost",
    #    port=3306,
    # )
    # print("Testing connection:")
    # print("Returned value:", engine)
    # print("Returned value type:", type(engine))

    # Testing connection.
    ctifnoexResult = create_table_if_not_exists(HeroModel)
    print("\nTesting create table if not exists:")
    print("Returned value:", ctifnoexResult)
    print("Returned value type:", type(ctifnoexResult))
