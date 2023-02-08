import os

new_directory = os.chdir('sql_scr')
new_directory_files=os.listdir(new_directory)
create_customers_script = new_directory_files[1]

def create_customers():
    script = []
    for line in open(create_customers_script):
        script.append(line)
    return script