# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


from dota2learning.database import get_connection
from dota2learning.database import close_connection


if __name__ =="__main__":

    # Test get_connection.
    #connection = get_connection(database_name="dota2learning")
    #print(type(connection))
    #print(bool(connection))


    # Test clo_connection
    #close = close_connection(connection)
    #print(type(close))
    #print(bool(close))


    # Create Hero table from ready SQL Script.
    #create_table(hero_table)


    # Insert data into Hero Table.
    #insert_data_into_table(insert_into_hero_table, get_heroes_stats())


    #hero_names = get_hero_names_from_database(500)
    #print(type(hero_names))
    #print(hero_names)
