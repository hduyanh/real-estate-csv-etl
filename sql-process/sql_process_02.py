import os
import db_connection

new_directory = os.chdir('sql-scripts')
new_directory_files=os.listdir(new_directory)
select_create_db_script = new_directory_files[1]
#sql_con = exec(open(create_db_script).read())

mycursor = db_connection.sql_connector.cursor()

for line in open(select_create_db_script):
    mycursor.execute(line)
print('Created customer table.')