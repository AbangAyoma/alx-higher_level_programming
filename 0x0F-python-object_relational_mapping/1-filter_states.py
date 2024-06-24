#!/bin/usr/python3
'''importing MySQLdb module to enable connection MySQL server'''
import MySQLdb
'''importing sys module to enable system args and kwargs'''
import sys

def users(username, password, database):
    """
    A function that connect to mysql database

    arguments:
    @username: username to connect to mysql
    @password: mysql password
    @database: database to use

    Returns:
    return None
   
    """
    db = MySQLdb.connect(
            host = 'localhost',
            port = 3306,
            user = username,
            passwd = password,
            db = db_name)
    #create a cursor object
    cursor = db.cursor()

    cursor.execute("SELECT id FROM states

