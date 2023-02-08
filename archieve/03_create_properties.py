import os

new_directory = os.chdir('sql_scr')
new_directory_files=os.listdir(new_directory)
create_properties_script = new_directory_files[2]

def create_properties():
    script = []
    for line in open(create_properties_script):
        script.append(line)
    return script