# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


from dota2learning.database import create_table, insert_data_into_table, get_hero_names_from_database



if __name__ =="__main__":

    # Create Hero table from ready SQL Script.
    #create_table(hero_table)

    # Insert data into Hero Table.
    #insert_data_into_table(insert_into_hero_table, get_heroes_stats())

    hero_names = get_hero_names_from_database(500)
    print(type(hero_names))
    print(hero_names)
