import pandas as pd


def file_reader(file_name, seperator):
    return pd.read_csv(file_name, seperator)

def file_information(file_data):
    length_rows = len(file_data)
    length_columns = len(file_data.columns)
    columns_header = list(file_data.columns)
    df_data_type = file_data.dtypes
    print(f"This file has: {length_rows} rows, and {length_columns} columns.\nColumns: \n{columns_header}\nDatatypes:\n{df_data_type}")