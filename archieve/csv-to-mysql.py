import pandas as pd
import mysql.connector
import os
import warnings

warnings.filterwarnings('ignore')

CURRENT_FILE_NAME = 'real_es.csv'
FILE_SEPERATOR = ','


def file_reader(file_name, seperator):
    return pd.read_csv(file_name, seperator)

def file_information(file_data):
    length_rows = len(file_data)
    length_columns = len(file_data.columns)
    columns_header = list(file_data.columns)
    df_data_type = file_data.dtypes
    print(f"This file has: {length_rows} rows, and {length_columns} columns.\nColumns: \n{columns_header}\nDatatypes:\n{df_data_type}")

def save_nan_to_csv(file_data):
    missing_values = file_data[file_data.isna().any(axis=1)]
    missing_values.fillna('missing data', inplace=True)
    os.makedirs('/Users/hoangduyanh/Documents/PythonProjects/python-etl/NaN', exist_ok=True)  
    missing_values.to_csv('/Users/hoangduyanh/Documents/PythonProjects/python-etl/NaN/NaN.csv')

def file_cleaner(file_data):
    df = file_data[~file_data.isna().any(axis=1)] # drop NaN
    df['Price'] = df['Price'].str.replace('$','').str.replace(',','').astype(float) # convert price to float
    df['Square meter'] = (df['Area (ft.)'] * 0.09290304).round(2) # convert feet to meter
    df['Price per meter'] = (df['Price'] / df['Square meter']).round(2) # calculate price/meter
    df['Sales ID'] = df['ID'].map(str) + df['Customer ID'] # generate sales ID
    df[['Year of sale', 'Month of sale', 'Y', 'M', 'D']] = df[['Year of sale', 'Month of sale', 'Y', 'M', 'D']].astype(int) # convert to integer
    return(df)

def customers_table(clean_file):
    customer_table = clean_file[['Customer ID', 'Name', 'Surname', 'Gender']]
    rename_customer = customer_table.rename(columns={"Customer ID": "customer_id","Name": "name","Surname": "surname", "Gender": "gender"})
    final_customer_table = rename_customer.drop_duplicates(subset='customer_id', keep='last')
    return final_customer_table

def properties_table(clean_file):
    property_table = clean_file[['ID', 'Building', 'Type of property', 'Property #', 'Area (ft.)', 'Status', 'Square meter', 'Customer ID','Country', 'State']]
    rename_property = property_table.rename(columns={'ID': "id", 'Building': 'building', 'Type of property': 'type_of_property', 'Property #': 'property_no','Area (ft.)':\
     'area_in_ft', 'Status': 'status', 'Square meter': 'square_meter', 'Customer ID': 'customer_id','Country': 'country', 'State': 'state'})
    final_property_table = rename_property.drop_duplicates(subset='id', keep='last')
    return final_property_table


def sales_table(clean_file):
    sale_table = clean_file[['Sales ID', 'Year of sale', 'Month of sale', 'Price', 'Deal satisfaction', 'Mortgage', 'Price per meter', 'ID', 'Entity', 'Purpose', 'Source']]
    rename_sale = sale_table.rename(columns={'Sales ID': 'sales_id', 'Year of sale': 'year_of_sale', 'Month of sale': 'month_of_sale', 'Price': 'price',\
        'Deal satisfaction': 'deal_satisfaction', 'Mortgage': 'mortgage', 'Price per meter': 'price_per_meter', 'ID': 'id', 'Entity': 'entity', 'Purpose': 'purpose', 'Source': 'source'})
    return rename_sale


def process():
    file_data = file_reader(CURRENT_FILE_NAME, FILE_SEPERATOR)
    file_info = file_information(file_data)
    save_csv = save_nan_to_csv(file_data)
    clean_file = file_cleaner(file_data)
    customers = customers_table(clean_file)
    property = properties_table(clean_file)
    sales = sales_table(clean_file)
    


# starting point of file
if __name__ == '__main__':
    process()