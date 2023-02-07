import pandas as pd
import warnings
import sys
sys.path.append(r'D:\Git\real-estate-csv-etl\config')
from config.config import engine

warnings.filterwarnings('ignore')

def customers_table(clean_file):
    customer_table = clean_file[['Customer ID', 'Name', 'Surname', 'Gender']]
    rename_customer = customer_table.rename(columns={'Customer ID': 'customer_id','Name': 'first_name','Surname': 'surname', 'Gender': 'gender'})
    final_customer_table = rename_customer.drop_duplicates(subset='customer_id', keep='last')
    final_customer_table.set_index('customer_id', inplace=True)
    final_customer_table.to_sql('customers', engine, if_exists = 'append')
#    return final_customer_table

def properties_table(clean_file):
    property_table = clean_file[['ID', 'Building', 'Type of property', 'Property #', 'Area (ft.)', 'Status', 'Square meter', 'Customer ID','Country', 'State']]
    rename_property = property_table.rename(columns={'ID': 'property_id', 'Building': 'building', 'Type of property': 'property_type', 'Property #': 'property_tier','Area (ft.)':\
     'area', 'Status': 'property_status', 'Square meter': 'square_meter', 'Customer ID': 'customer_id','Country': 'country', 'State': 'property_state'})
    final_property_table = rename_property.drop_duplicates(subset='property_id', keep='last')
    final_property_table.set_index('property_id', inplace=True)
    final_property_table.to_sql('properties', engine, if_exists = 'append')
#    return final_property_table

def sales_table(clean_file):
    sale_table = clean_file[['Sales ID', 'Year of sale', 'Month of sale', 'Price', 'Deal satisfaction', 'Mortgage', 'Price per meter', 'ID', 'Entity', 'Purpose', 'Source', 'Age at time of purchase', 'Customer ID', 'D', 'Interval', 'M', 'Y']]
    rename_sale = sale_table.rename(columns={'Sales ID': 'sales_id', 'Year of sale': 'year_of_sale', 'Month of sale': 'month_of_sale', 'Price': 'price',\
        'Deal satisfaction': 'deal_status', 'Mortgage': 'mortgage', 'Price per meter': 'meter_price', 'ID': 'property_id', 'Entity': 'entity', 'Purpose': 'purpose', 'Source': 'source', 'Age at time of purchase': 'age_of_buy', \
            'Customer ID': 'customer_id', 'Interval': 'interval_time'})
    rename_sale.set_index('sales_id', inplace=True)
    rename_sale.to_sql('sales', engine, if_exists = 'append')
#    return rename_sale