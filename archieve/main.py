from config.logger import logger
import mysql.connector as mysql
from archieve.db_connection_singleton import MySQLConnection


def main() -> None:
    try:
       credentials = {
          "host": 'localhost',
          "user": 'root',
          "password": '123456'
       }
       conn_mysql = MySQLConnection.get_instance(credentials)
       logger.info(f'MySQL database connected successfully: {conn_mysql}')
       query = "CREATE DATABASE IF NOT EXISTS real_estate;"
       MySQLConnection.execute_query(query)
       logger.info(f'Database created successfully: real_estate')
       query = 'USE real_estate;'            
       MySQLConnection.execute_query(query)
       logger.info(f'Using table successfully: real_estate')
#       MySQLConnection.close_instance()
#       logger.info(f'MySQL database closed successfully: {conn_mysql}')
    except TypeError as error:
       logger.error(f'Error to connect to MySQL database: {error}')


if __name__ == "__main__":
   main()


'''
  logolas, print helyet :3 szint :3 info(amikor vlamit ortenik a kodban) warn(tortenik ami kjiszamithatalan, de megis megtortent de megis megtortent) error(fatal hiba)
  
  os , listazni es  vegremenjen sorrenben(szamokkal h ugy fussanak le)

  cisnalni sql procces, etl process
  csinalni database connection.py

  3 table : sales,properties,customers ... atadni sql-be (ezek jelenleg egzybe vannak)
'''
  