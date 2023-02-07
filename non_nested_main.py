from config.logger import logger
from config.config import *
from src.mysql_singleton import Singeleton_DB
from src.extract import *
from src.transform import *
from src.load import *


def main():

    try:
        conn_mysql = Singeleton_DB.getInstance()
        logger.info(f'MySQL database connected successfully: {conn_mysql}')
    except TypeError as error:
        logger.error(f'Error to connect to MySQL database: {error}')
    pass

    try:
        scripts = [
        'CREATE DATABASE IF NOT EXISTS real_estate;'
        ]
        Singeleton_DB.script_executer(scripts)
        logger.info('Using real_estate')
    except TypeError as error:
        logger.error(f'Error using real_estate')
    pass

    try:
        scripts = [
        'USE real_estate;', 
        'DROP TABLE IF EXISTS customers;', 
        'CREATE TABLE customers (customer_id VARCHAR(30), first_name VARCHAR(30), surname VARCHAR(30), gender VARCHAR(30), PRIMARY KEY (customer_id));'
        ]
        Singeleton_DB.script_executer(scripts)
        logger.info(f'Created table successfully: customer')
    except TypeError as error:
        logger.error(f'Error to create table: customer')
    pass

    try:
        scripts = [
        'USE real_estate;', 
        'DROP TABLE IF EXISTS properties;', 
        'CREATE TABLE properties (property_id VARCHAR(30), building INT, property_type VARCHAR(30), property_tier INT, area VARCHAR(30), property_status VARCHAR(30), square_meter FLOAT(10,2),\
        country VARCHAR(30), property_state VARCHAR(30), customer_id VARCHAR(30), PRIMARY KEY (property_id), FOREIGN KEY (customer_id) REFERENCES customers(customer_id));'
        ]
        Singeleton_DB.script_executer(scripts)
        logger.info(f'Created table successfully: properties')
    except TypeError as error:
        logger.error(f'Error to create table: properties')
    pass

    try:
        scripts = [
        'USE real_estate;', 
        'DROP TABLE IF EXISTS sales;', 
        'CREATE TABLE sales (sales_id VARCHAR(30), source VARCHAR(30), year_of_sale YEAR, month_of_sale INT, price INT, deal_status VARCHAR(30), mortgage VARCHAR(30), meter_price FLOAT(10,2), property_id VARCHAR(30), customer_id VARCHAR(30), entity VARCHAR(30), purpose VARCHAR(30),\
        age_of_buy INT, interval_time VARCHAR(30), y INT, M INT, D INT, PRIMARY KEY (sales_id), FOREIGN KEY (customer_id) REFERENCES customers(customer_id), FOREIGN KEY (property_id) REFERENCES properties(property_id));'
        ]
        Singeleton_DB.script_executer(scripts)
        logger.info(f'Created table successfully: sales')
    except TypeError as error:
        logger.error(f'Error to create table: sales')
    pass

    try:
    # file_information not executed
        read_file = file_reader(csv_config['file_name'], csv_config['seperator'])
        logger.info('File extracted')
    except TypeError as error:
        logger.error('Error while extracting file')
    pass

    try:
        save_nan_to_csv(read_file)
        cleaned_file = file_cleaner(read_file)
        logger.info('File transformed, files with NaN saved to csv')
    except TypeError as error:
        logger.error('Error while transforming file/saving NaN')
    pass

    try:
        customers_table(cleaned_file)
        logger.info('Loaded customers to SQL')
    except TypeError as error:
        logger.error('Error while loading customers to SQL')
    pass

    try:
        properties_table(cleaned_file)
        logger.info('Loaded properties to SQL')
    except TypeError as error:
        logger.error('Error while loading properties to SQL')
    pass

    try:
        sales_table(cleaned_file)
        logger.info('Loaded sales to SQL')
    except TypeError as error:
        logger.error('Error while loading sales to SQL')
    pass

if __name__ == '__main__':
    main()
