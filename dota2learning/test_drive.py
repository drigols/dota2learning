# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


from dota2learning.database import get_connection
from dota2learning.database import close_connection
from dota2learning.database import create_table
from dota2learning.database import insert_data_into_table

from dota2learning.api.opendota import get_heroes_stats

from dota2learning.sql.create_table import hero_table
from dota2learning.sql.create_table import invalid_table
from dota2learning.sql.insert_queries import insert_into_hero_table


if __name__ =="__main__":

    #pass
    # Test get_connection.
    #print("\nTesting database connection:")
    #connection = get_connection(database_name="dota1learning")
    #print(type(connection))
    #print(bool(connection))


    # Test close_connection.
    #print("\nTesting close connection:")
    #close = close_connection(connection)
    #print(type(close))
    #print(bool(close))


    # Create Hero table from ready SQL Script.
    #print("\nTesting create valid table:")   
    result_valid = create_table(hero_table)
    #print(type(result_valid))
    #print(bool(result_valid))


    # Create Hero table from ready SQL Script.
    #print("\nTesting create invalid table:")  
    #result_invalid = create_table(invalid_table)
    #print(type(result_invalid))
    #print(bool(result_invalid))


    # Insert data into Hero Table.
    #print("\nTesting insert data into table:")  
    #result_insert = insert_data_into_table(insert_into_hero_table, get_heroes_stats())
    #print(type(result_insert))
    #print(bool(result_insert))

    #hero_names = get_hero_names_from_database(500)
    #print(type(hero_names))
    #print(hero_names)
