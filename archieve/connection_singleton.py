from typing import Dict
import mysql.connector as mysql

class MySQLConnection:

    __instance = None

    def __init__(self, host: str, user: str, password: str) -> None:
        self.host = host
        self.user = user
        self.password = password
        if MySQLConnection.__instance is None:
            MySQLConnection.__instance = mysql.connect(host=self.host, user=self.user, passwd=self.password)
        else:
            raise Exception('You cannot create another MySQL connection')

    @staticmethod
    def get_instance(credentials: Dict[str, str]) -> object:
        if not MySQLConnection.__instance:
            MySQLConnection(credentials['host'], credentials['user'], credentials['password'])
        return MySQLConnection.__instance

    @staticmethod
    def close_instance() -> None:
        MySQLConnection.__instance.close()