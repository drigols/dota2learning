# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


import mysql.connector
from mysql.connector import Error

from dota2learning.api.opendota import get_heroes_stats

from sql.create_table import hero_table
from sql.insert_queries import insert_into_hero_table


def get_connection():
  try:
    connection = mysql.connector.connect(
      host='localhost',
      database='dota2learning',
      user='root',
      password='toor'
    )
    if connection.is_connected():
      db_Info = connection.get_server_info()
      print("Connected to MySQL Server version ", db_Info)
      cursor = connection.cursor()
      cursor.execute("select database();")
      record = cursor.fetchone()
      print("You're connected to database:", record)
  except Exception as error:
    return print("Error while connecting to MySQL", error)
  else:
    return connection


def close_connection(connection):
  if connection.is_connected:
    connection.close()
    print("MySQL connection is closed.\n")


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


if __name__ =="__main__":

  # Create Hero table from ready SQL Script.
  create_table(hero_table)

  # Insert data into Hero Table.
  insert_data_into_table(insert_into_hero_table, get_heroes_stats())

