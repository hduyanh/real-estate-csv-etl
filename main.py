from config.logger import logger
from config.config import *
from src.mysql_singleton import Singeleton_DB
from src.extract import *
from src.transform import *
from src.load import *
from src.sql_to_dic import *


def main():

    try:
        conn_mysql = Singeleton_DB.getInstance()
        logger.info(f'MySQL database connected successfully: {conn_mysql}')
    except TypeError as error:
        logger.error(f'Error to connect to MySQL database: {error}')
    pass

    try:
        scripts = create_db()
        Singeleton_DB.script_executer(scripts)
        logger.info('Using real_estate')
    except TypeError as error:
        logger.error(f'Error using real_estate')
    pass

    try:
        scripts = create_customers()
        Singeleton_DB.script_executer(scripts)
        logger.info(f'Created table successfully: customer')
    except TypeError as error:
        logger.error(f'Error to create table: customer')
    pass

    try:
        scripts = create_properties()
        Singeleton_DB.script_executer(scripts)
        logger.info(f'Created table successfully: properties')
    except TypeError as error:
        logger.error(f'Error to create table: properties')
    pass

    try:
        scripts = create_sales()
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
