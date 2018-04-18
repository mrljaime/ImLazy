# --*-- encoding: utf-8 --*-- 

import os
from mysql.connector import (connection)
from logger import logging

class DBManager():
    
    MAX_RETRIES = 5
    
    connection = None
    retries = 0
    
    def __init__(self, host="", user="", password="", database=""):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
    def connect(self):
        logging.debug("Trying to connect to MariaDB server on host '%s' with user '%s' and password '*****' on '%s' database"
            % (self.host, self.user, self.database))
        self.connection = connection.MySQLConnection(host=self.host, 
                                                     user=self.user, 
                                                     password=self.password, 
                                                     database=self.database)

    def select(self, sql, params):
        """
        :param string sql 
        :param dictionary args 
        """
        if self.connection is None:
            self.connect()
            self.select(sql, params)
            if self.retries == self.MAX_RETRIES:
                os.exit(1)
            
            self.retries += 1
        else:
            self.connection.close()
            self.connect()
            
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, params)
            logging.info("Executed query: %s" % cursor.statement)
        except:
            logging.error("Error on query: %s" % cursor.statement)
            cursor = []
        
        return cursor
        