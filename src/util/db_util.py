"""
Handles all database functions
"""
import os

from pymongo import MongoClient


class DBUtil:
    """
    Handles all database communications
    """

    db_port = os.environ.get('DB_PORT', 27017)
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_password = os.environ.get('DB_PASSWORD', 'password')
    db_user = os.environ.get('DB_USER', 'root')
    db_auth_mech = "SCRAM-SHA-1"

    def __init__(self, db_name="resume-api"):
        self.client = MongoClient(
            self.db_host,
            port=self.db_port,
            username=self.db_user,
            password=self.db_password,
            authMechanism=self.db_auth_mech
        )
        self.db_client = self.client[db_name]

    def get_db(self):
        """
        Returns DB client
        """
        return self.db_client

    def get_collection(self, collection_name):
        """ Returns collection """
        return self.db_client[collection_name]

    def close_db_conection(self):
        """ Terminate Database connection """
        return self.client.close()
