# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from dota2learning.api.opendota import get_heroes_stats
from dota2learning.database.connections import close_connection
from dota2learning.database.connections import get_connection
from dota2learning.database.create_tables import create_table
from dota2learning.database.get_from_database import (
    get_hero_names_from_database,
)
from dota2learning.database.inserts import insert_data_into_table
from dota2learning.sql.create_table import hero_table
from dota2learning.sql.create_table import invalid_table
from dota2learning.sql.insert_queries import insert_into_hero_table


if __name__ == "__main__":

    # Test get_connection.
    # print("\nTesting database connection:")
    # connection = get_connection()
    # print(type(connection))
    # print(bool(connection))

    # Test close_connection.
    # print("\nTesting close connection:")
    # close = close_connection(connection)
    # print(type(close))
    # print(bool(close))

    # Create Hero table from ready SQL Script.
    # print("\nTesting create valid table:")
    # result_valid = create_table(hero_table)
    # print(type(result_valid))
    # print(bool(result_valid))

    # Insert data into Hero Table.
    # print("\nTesting insert data into table:")
    # result_insert = insert_data_into_table(
    #     insert_into_hero_table, get_heroes_stats()
    # )
    # print(type(result_insert))
    # print(bool(result_insert))

    hero_names = get_hero_names_from_database(1)
    print(type(hero_names))
    print(hero_names)
