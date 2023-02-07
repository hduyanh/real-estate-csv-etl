from typing import Dict
from src.logger import logger
import mysql.connector as mysql
import time


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
'''
    @staticmethod
    def close_instance() -> None:
        MySQLConnection.__instance.close()
'''


def main() -> None:
    try:
       credentials = {
          "host": 'localhost',
          "user": 'root',
          "password": '123456'
       }
       conn_mysql = MySQLConnection.get_instance(credentials)
       logger.info(f'MySQL database connected successfully: {conn_mysql}')
#       time.sleep(10)
#       MySQLConnection.close_instance()
#       logger.info(f'MySQL database closed successfully: {conn_mysql}')
    except TypeError as error:
       logger.error(f'Error to connect to MySQL database: {error}')


if __name__ == "__main__":
   main()