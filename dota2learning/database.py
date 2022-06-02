# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


from unicodedata import name
import mysql.connector
from mysql.connector import Error

from dota2learning.api.opendota import get_heroes_stats

from dota2learning.sql.create_table import hero_table
from dota2learning.sql.insert_queries import insert_into_hero_table
from dota2learning.sql.select_queries import get_names_query


def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dota2learning',
            user='root',
            password='toor'
        )
    except Exception as error:
        return print("Error while connecting to MySQL", error)
    else:
        return connection


def close_connection(connection):
    if connection.is_connected:
        connection.close()


def create_table(sql_script=None):
    if sql_script == None:
        return print("Please, enter your SQL Script to Create Table.")
    else:
        try:
            connection = get_connection()
            cursor = connection.cursor()
            result = cursor.execute(sql_script)
            print("Table created successfully!")
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            cursor.close()
            close_connection(connection)


def insert_data_into_table(insert_query=None, records_to_insert=None):
    if insert_query == None:
        return print("Please, enter your SQL Script to insert data in the table.")
    elif records_to_insert == None:
        return print("Please, enter your records data to insert data in the table.")
    else:
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.executemany(insert_query, records_to_insert)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into table.")
        except mysql.connector.Error as error:
            return print("Failed to insert record into MySQL table: {}".format(error))
        finally:
            cursor.close()
            close_connection(connection)


def get_hero_names_from_database(id: int) -> dict:
    """Get hero names by ID from the Database.

    Args:
        id (int): Hero ID.

    Returns:
        dict: The return is a dictionary contain hero names.
        The dictionary have the follows keys "localized_name"
        and yours respective values.
    """
    hero_names = {}
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(get_names_query, (id,))
        names = cursor.fetchall()
        for name in names:
            hero_names = {
                "name": name[0],
                "localized_name": name[1]
            }
    except mysql.connector.Error as error:
        print("Failed to select hero names: {}".format(error))
    finally:
        cursor.close()
        close_connection(connection)
    # Check if SELECT query return is empty, that's, don't have hero with this ID.
    if hero_names:
        return hero_names
    else:
        print("There is no hero with this ID.")
        return None
