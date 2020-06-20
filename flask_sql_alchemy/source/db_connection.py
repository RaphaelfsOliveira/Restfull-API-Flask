import sqlite3
import functools


def db_manage(func, query , *args):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    result = func(query, *args, cursor=cursor, conn=connection)

    connection.close()
    return result

def make_query(query, *args, **kwargs):
    kwargs['cursor'].execute(query, (*args,))
    kwargs['conn'].commit()

def select_query(query, *args, **kwargs):
    result = kwargs['cursor'].execute(query, (*args,))
    result = result.fetchone()
    return result

def select_query_all(query, *args, **kwargs):
    result = kwargs['cursor'].execute(query)
    result = result.fetchall()
    return result