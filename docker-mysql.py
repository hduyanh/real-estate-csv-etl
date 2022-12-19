import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database = "flat_prices"
)
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE flat_prices")

#mycursor.execute("SHOW DATABASES")

#mycursor.execute("SHOW TABLES")

#mycursor.execute("CREATE TABLE customers (customer_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), surname VARCHAR(30), age_at_time_of_purchase TINYINT, age_interval VARCHAR(30), year TINYINT, month TINYINT, day TINYINT, gender VARCHAR(30))")


#sql = """INSERT INTO customers (customer_id, address, name, surname, age_at_time_of_purchase, age_interval, year, month, day, gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# creating column list for insertion
cols = "`,`".join([str(i) for i in c.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in customer_table.iterrows():
    sql = "INSERT INTO `book_details` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    mycursor.execute(sql, tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
    connection.commit()

'''
for x in mycursor:
  print(x)
'''


