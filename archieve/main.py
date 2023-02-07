import archieve.db_connection_singleton as connect


def main():

  connect.main()





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
  