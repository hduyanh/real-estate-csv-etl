from sqlalchemy import create_engine

CURRENT_FILE_NAME = r'D:\Git\real-estate-csv-etl\data\raw\real_es.csv'
FILE_SEPERATOR = ','

csv_config = {

        'file_name': CURRENT_FILE_NAME,
        'seperator': FILE_SEPERATOR,
    }


# mysql (target db)
mysql_db_config = {

    'host': 'localhost',
    'user': 'root',
    'password': '123456',
}

engine = create_engine("mysql://root:123456@localhost:3306/real_estate")
