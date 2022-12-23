import mysql.connector
import config.config as config

dir = r'/Users/hoangduyanh/Documents/Repositories/real-estate-csv-etl/sql-scripts/'

def main():
    print('starting etl...')

    # establish connection
    mydb = mysql.connector.connect(**config.mysql_db_config)
    print(f"connection succes: {mydb}")

    mycursor = mydb.cursor()
    # create db
    for line in open(f"{dir}create_db.sql"):
      mycursor.execute(line)
      print('db created')

if __name__ == "__main__":
  main()