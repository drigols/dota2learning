# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from dota2learning.api.opendota import get_heroes_stats
from dota2learning.database.connection import get_engine_connection
from dota2learning.database.create_table import create_table_if_not_exists
from dota2learning.database.inserts import insert_into_table
from dota2learning.database.settings import db_settings
from dota2learning.models.hero_model import HeroModel


if __name__ == "__main__":

    # Connection Testing.
    connEngine = get_engine_connection(**db_settings)
    print("\nConnection Testing:")
    print("Variable result:", connEngine)
    print("Type Result:", type(connEngine))
    print("Bool result:", bool(connEngine))

    # Create Table Testing.
    print("\nCreate Table Testing:")
    cTable = create_table_if_not_exists(model=HeroModel)
    print("Variable result:", cTable)
    print("Type Result:", type(cTable))
    print("Bool result:", bool(cTable))

    # Inser into Table Testing.
    print("\nInsert into Table Testing:")
    insertIntoHero = insert_into_table(HeroModel, get_heroes_stats())
    print("Variable result:", insertIntoHero)
    print("Type Result:", type(insertIntoHero))
    print("Bool result:", bool(insertIntoHero))
