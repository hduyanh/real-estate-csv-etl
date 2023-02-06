from test_connect import Database
import os

class BaseDAO():
    def __init__(self):
      # Create an instance of the database pool.
      self.db = Database()
      self.db.pool_size =3
      
      # For testing purposes lets print out the db
      print(self.db) 
