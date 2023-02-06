import os
import db_connection
import sys
sys.path.append(r'D:\Git\real-estate-csv-etl\config')
import config

new_directory = os.chdir('sql-scripts')
new_directory_files=os.listdir(new_directory)
select_create_db_script = new_directory_files[0]

mycursor = db_connection.sql_connector.cursor()

for line in open(select_create_db_script, 'r'):
    mycursor.execute(line)
    print('db created')
