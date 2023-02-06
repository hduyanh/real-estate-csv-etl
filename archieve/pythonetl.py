import pandas as pd
import mysql.connector

CURRENT_FILE_NAME = 'real_es.csv'
FILE_SEPERATOR = ','

read_file = pd.read_csv(CURRENT_FILE_NAME, FILE_SEPERATOR)

# information about the data
lenght_rows = len(read_file)
lenght_columns = len(read_file.columns)
columns_header = list(read_file.columns)
df_data_type = read_file.dtypes
top_5_columns = read_file.head(5)

missing_values = read_file[read_file.isna().any(axis=1)]

df = read_file[~read_file.isna().any(axis=1)]

df['Price'] = df['Price'].str.replace('$','').str.replace(',','').astype(float)

df['Square meter'] = (df['Area (ft.)'] * 0.09290304).round(2)
df['Price per meter'] = (df['Price'] / df['Square meter']).round(2)
df['Sales ID'] = df['ID'].map(str) + df['Customer ID']


#new_df[['square_meter', 'price_per_meter']].round(2)
df[['Year of sale', 'Month of sale', 'Y', 'M', 'D']] = df[['Year of sale', 'Month of sale', 'Y', 'M', 'D']].astype(int)

customer_table = df[['Customer ID', 'Name', 'Surname', 'Gender']]
final= customer_table.rename(columns={"Customer ID": "customer_id","Name": "name","Surname": "surname", "Gender": "gender"})
fixed = final.drop_duplicates()
print(len(fixed))
#########
'''
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

mycursor.execute("CREATE TABLE customers (customer_id VARCHAR(50), name VARCHAR(50), surname VARCHAR(50), gender VARCHAR(50))")

#mycursor.execute("ALTER TABLE customers modify customer_id int auto_increment primary key")

#sql = """INSERT INTO customers (customer_id, name, surname, age_at_time_of_purchase, age_interval, year, month, day, gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# creating column list for insertion
cols = "`,`".join([str(i) for i in fixed.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in fixed.iterrows():
    sql = "INSERT INTO `customers` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    mycursor.execute(sql, tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
    mydb.commit()
print(mycursor.rowcount, "record inserted.")
'''





