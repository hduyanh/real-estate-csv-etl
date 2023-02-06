import mysql.connector
class Singleton(object):

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'): 
            org = super(Singleton, cls)  
            cls._instance = org.__new__(cls, *args, **kw) 
        return cls._instance

class Database(Singleton):

   connection = None
   cursor = None

   def __init__(self):
      if Database.connection is None:
         try:
            Database.connection = mysql.connector.connect(host="localhost", user="root", password="123456")
            Database.cursor = Database.connection.cursor()
         except Exception as error:
            print("Error: Connection not established {}".format(error))
         else:
            print("Connection established")

      self.connection = Database.connection
      self.cursor = Database.cursor

class BaseDAO():
    def __init__(self):
      # Create an instance of the database pool.
      self.db = Database()
      self.db.pool_size =3
      
      # For testing purposes lets print out the db
      print(self.db) 

def process01():
      with Database() as cursor:
        cursor.execute('CREATE DATABASE IF NOT EXISTS real_estate;')


def main():
   Database()
   process01()

if __name__ == "__main__":
  main()