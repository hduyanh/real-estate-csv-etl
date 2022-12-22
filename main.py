import mysql.connector
import config.config as config



def main():
    print('starting etl...')

    # establish connection
    mydb = mysql.connector.connect(**config.mysql_db_config)
    print(f"connection succes: {mydb}")

    mycursor = mydb.cursor()
    # create db
    for line in open('create_db.sql'):
      mycursor.execute(line)
      print()
    
    

if __name__ == "__main__":
  main()