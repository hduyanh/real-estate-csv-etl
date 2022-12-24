import mysql.connector
import config.config as config

# establish connection
sql_connector = mysql.connector.connect(**config.mysql_db_config)
print(f"connection succes: {sql_connector}")