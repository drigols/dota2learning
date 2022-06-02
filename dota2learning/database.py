# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


import mysql.connector
from mysql.connector import Error

from dota2learning.api.opendota import get_heroes_stats

from dota2learning.sql.create_table import hero_table
from dota2learning.sql.insert_queries import insert_into_hero_table
from dota2learning.sql.select_queries import get_names_query


def get_connection(
    host_name='localhost',
    database_name='dota2learning',
    user_name='root',
    user_password='toor'
):
    """Create connection on Dota2Learning Database.

    Args:
        host_name (str, optional): Hostname from your MySQL Server. Defaults to 'localhost'.
        database_name (str, optional): Database name. Defaults to 'dota2learning'.
        user_name (str, optional): User name. Defaults to 'root'.
        user_password (str, optional): User password. Defaults to 'toor'.

    Returns:
        <class 'mysql.connector.connection_cext'>: The return is a MySQL connection.
    """
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        )
    except Exception as error:
        print("Error while connecting to MySQL - ", error)
    else:
        return connection


def close_connection(connection):
    """_summary_

    Args:
        connection (mysql.connector.connection_cext): The argument received is a MySQL connection.

    Returns:
        bool: The original return was False when database connection was closed.
        But, I forced that return was True when database connection was closed.
    """
    if connection.is_connected:
        connection.close()
        return True # Force return True.


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
