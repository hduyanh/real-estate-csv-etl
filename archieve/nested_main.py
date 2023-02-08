from src.mysql_singleton import Singeleton_DB
import sys
sys.path.append(r'D:\Git\real-estate-csv-etl')
from config.logger import logger


def main():
    try:
        conn_mysql = Singeleton_DB.getInstance()
        logger.info(f'MySQL database connected successfully: {conn_mysql}')
        try:
            scripts = [
            'CREATE DATABASE IF NOT EXISTS real_estate;'
            ]
            Singeleton_DB.script_executer(scripts)
            logger.info('Using real_estate')
            try:
                scripts = [
                'USE real_estate;', 
                'DROP TABLE IF EXISTS customers;', 
                'CREATE TABLE customers (customer_id VARCHAR(30), first_name VARCHAR(30), surname VARCHAR(30), gender VARCHAR(30), PRIMARY KEY (customer_id));'
                ]
                Singeleton_DB.script_executer(scripts)
                logger.info(f'Created table successfully: customer')
                try:
                    scripts = [
                    'USE real_estate;', 
                    'DROP TABLE IF EXISTS properties;', 
                    'CREATE TABLE properties (property_id VARCHAR(30), building INT, property_type VARCHAR(30), property_tier INT, area VARCHAR(30), property_status VARCHAR(30), square_meter FLOAT(10,2),\
                    country VARCHAR(30), property_state VARCHAR(30), customer_id VARCHAR(30), PRIMARY KEY (property_id), FOREIGN KEY (customer_id) REFERENCES customers(customer_id));'
                    ]
                    Singeleton_DB.script_executer(scripts)
                    logger.info(f'Created table successfully: properties')
                    try:
                        scripts = [
                        'USE real_estate;', 
                        'DROP TABLE IF EXISTS sales;', 
                        'CREATE TABLE sales (sales_id VARCHAR(30), year_of_sale YEAR, month_of_sale INT, price INT, deal_status VARCHAR(30), mortgage VARCHAR(30), meter_price FLOAT(10,2), property_id VARCHAR(30), customer_id VARCHAR(30), entity VARCHAR(30), purpose VARCHAR(30),\
                        age_of_buy INT, interval_time VARCHAR(30), y INT, M INT, D INT, PRIMARY KEY (sales_id), FOREIGN KEY (customer_id) REFERENCES customers(customer_id), FOREIGN KEY (property_id) REFERENCES properties(property_id));'
                        ]
                        Singeleton_DB.script_executer(scripts)
                        logger.info(f'Created table successfully: sales')
                    except TypeError as error:
                        logger.error(f'Error to create table: sales')
                except TypeError as error:
                        logger.error(f'Error to create table: properties')
            except TypeError as error:
                    logger.error(f'Error to create table: customer')
        except TypeError as error:
            logger.error(f'Error using real_estate')
    except TypeError as error:
        logger.error(f'Error to connect to MySQL database: {error}')

if __name__ == '__main__':
    main()
