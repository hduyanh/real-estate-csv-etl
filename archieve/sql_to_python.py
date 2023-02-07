import os
import sys
sys.path.append(r'D:\Git\real-estate-csv-etl')

# list all the sql scripts
def sql_file_map():
    new_directory = os.chdir('sql_scripts')
    sql_files = os.listdir(new_directory)
    return sql_files

# conver sql scripts to python dictionary
def sql_filtes_to_dic(sql_file):
    empty_dic = []
    for line in open(sql_file):
        empty_dic.append(line)
    return empty_dic
