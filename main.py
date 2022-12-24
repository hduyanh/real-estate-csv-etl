import os

def main():
    print('starting etl...')

    # establish sql connection 
    sql_con = exec(open("db_connection.py").read())

    sql_1 = exec(open("sql_process_01.py").read())







'''
    mycursor = mydb.cursor()
    # create db
    for line in open(f"{dir}create_db.sql"):
      mycursor.execute(line)
      print('db created')
'''

if __name__ == "__main__":
  main()

  '''

  logolas, print helyet :3 szint :3 info(amikor vlamit ortenik a kodban) warn(tortenik ami kjiszamithatalan, de megis megtortent de megis megtortent) error(fatal hiba)
  
  os , listazni es  vegremenjen sorrenben(szamokkal h ugy fussanak le)

  cisnalni sql procces, etl process
  csinalni database connection.py

  3 table : sales,properties,customers ... atadni sql-be (ezek jelenleg egzybe vannak)
  '''
  