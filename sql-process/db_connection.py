import mysql.connector
import sys
sys.path.append(r'D:\Git\real-estate-csv-etl\config')
import config

# establish connection
sql_connector = mysql.connector.connect(**config.mysql_db_config)
print(f"connection succes: {sql_connector}")