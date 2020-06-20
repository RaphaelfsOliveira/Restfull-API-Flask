import sqlite3
import functools


def select_query(query, *args):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    result = cursor.execute(query, (*args,))
    row = result.fetchone()

    connection.close()
    return row

def select_query_all(query, *args):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    result = cursor.execute(query)
    row = result.fetchall()

    connection.close()
    return row

def create_query(query, *args):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    result = cursor.execute(query, (*args,))
    
    connection.commit()    
    connection.close()