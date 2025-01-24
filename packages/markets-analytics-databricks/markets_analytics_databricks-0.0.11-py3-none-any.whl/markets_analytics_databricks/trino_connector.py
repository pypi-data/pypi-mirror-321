import pandas as pd
import datetime as dt

from trino.dbapi import connect
from gsheet_helper import GSheetHelper
from trino.auth import JWTAuthentication

class TrinoConnector:
    def __init__(self, credentials, host="interactive.starburst.zalando.net", port=443, catalog="hive"):
        """
            Initializing connection details and testing out the connection to Superset
        """
        self.host = host
        self.port = port
        self.catalog = catalog
        self.__credentials__ = credentials

        self.__connect__()

    def __connect__(self):
        """
            Connecting to the Superset Server instance
        """
        gsheet = GSheetHelper("1Bw1PmPnIgx3RqEHFuMhtKDeFUBm-OzDhuEO_9GwZCRY", self.__credentials__)
        self.__user__ = gsheet.read("Token", "A2", header=False, log=False)
        pwd = gsheet.read("Token", "B2", header=False, log=False)

        self.__conn__ = connect(
            host=self.host,
            port=self.port,
            catalog=self.catalog,
            user=self.__user__,
            auth=JWTAuthentication(pwd),
            http_scheme="https"
        )
    
    def __disconnect__(self):
        """
            Disconnecting from the Superset Server instance
        """
        self.__conn__.close()
    
    def __str__(self):
        """
            Printing which user is connected to what instance of Superset Server
        """
        if self.__user__ is None:
            return "No connection has been made to any Datalake instance"
        return f"Username `{self.__user__}` connected to Datalake host: {self.host}:{self.port}/{self.catalog}"
    
    def execute(self, query, log=True):
        """
            Executing the SQL query and returning it as a Pandas DataFrame
        """
        if log: print(f"[{dt.datetime.now()}] Executing Query\n{query}")

        self.__connect__()
        df = pd.read_sql_query(query, self.__conn__)
        self.__disconnect__()

        if log: print(f"[{dt.datetime.now()}] Query Executed Successfully")

        return df