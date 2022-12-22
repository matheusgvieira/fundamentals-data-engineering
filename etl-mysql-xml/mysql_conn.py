"""
This module is used to connect to a mysql database
"""

from os import getenv

import mysql.connector


class Mysql:
    """
    This class is used to connect to a mysql database
    """

    def __init__(
        self,
        host: str = str(),
        port: str = str(),
        username: str = str(),
        password: str = str(),
    ):
        """
        Create a connection to a mysql database

        :param host: host of the database
        :param port: port of the database
        :param username: username of the database
        :param password: password of the database
        return: None
        """
        self.user = username or getenv("MYSQL_USER")
        self.password = password or getenv("MYSQL_PASSWORD")
        self.host = host or getenv("MYSQL_HOST")
        self.port = port or getenv("MYSQL_PORT")
        self.conn = mysql.connector.connect(
            user=self.user, password=self.password, host=self.host, port=self.port
        )
        self.cursor = self.conn.cursor()

    def query(self, query: str) -> list:
        """
        Execute a query
        query: query to be executed
        return: result of the query
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, query: str) -> None:
        """
        Insert data into a table
        query: query to be executed
        return: None
        """
        self.cursor.execute(query)
        self.conn.commit()
