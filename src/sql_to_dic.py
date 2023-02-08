import os

new_directory = os.chdir('sql_scr')
new_directory_files=os.listdir(new_directory)
create_db_script = new_directory_files[0]
create_customers_script = new_directory_files[1]
create_properties_script = new_directory_files[2]
create_sales_script = new_directory_files[3]


def create_db():
    script = []
    for line in open(create_db_script):
        script.append(line)
    return script

def create_customers():
    script = []
    for line in open(create_customers_script):
        script.append(line)
    return script

def create_properties():
    script = []
    for line in open(create_properties_script):
        script.append(line)
    return script

def create_sales():
    script = []
    for line in open(create_sales_script):
        script.append(line)
    return script