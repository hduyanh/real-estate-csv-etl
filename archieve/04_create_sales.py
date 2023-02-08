import os

new_directory = os.chdir('sql_scr')
new_directory_files=os.listdir(new_directory)
create_sales_script = new_directory_files[3]

def create_sales():
    script = []
    for line in open(create_sales_script):
        script.append(line)
    return script