#!/usr/bin/python3
""" importing MySQLdb module for linking of MySQL with python code"""
import MySQLdb
"""importing sys module to enable command line args"""
import sys

def list_states(username, password, db_name):
     """
      Connects to a MySQL database and lists all states in the 'states' table.

       Args:
        username (str): The username to connect to the MySQL server.
        password (str): The password to connect to the MySQL server.
        db_name (str): The name of the database to connect to.

      Returns:
        None 
      """

     try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        # Create a cursor object
        cursor = db.cursor()
        """creating the cursor"""

        # Execute the SQL query to select all states sorted by id
        cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

        # Fetch all the results
        states = cursor.fetchall()

        # Print the results
        for state in states:
            print(state)

     except MySQLdb.Error as e:
        print(f"Error: {e}")
     finally:
        if db:
            db.close()

if __name__ == "__main__":

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db_name)
