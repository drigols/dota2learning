# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


import mysql.connector

from dota2learning.database.connections import get_connection, close_connection


def create_table(sql_script: str) -> bool:
    """Function to create tables.

    Args:
        sql_script (str): SQL query to create a table.

    Returns:
        bool: The return is a True when create the table
              and False when create except.
    """
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            result = cursor.execute(sql_script)
            print("Table created successfully!")
            cursor.close()
            close_connection(connection)
            return True
    except mysql.connector.Error as error:
        print(error)
        return False
