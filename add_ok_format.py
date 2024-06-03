import os 
import re

def add_line(path, str):
    filename = os.path.basename(path)
    if not bool(re.match(r"^q\d+\w*\.py$", filename)):
        return
    with open(path, "a") as f:
        f.write("{0}\n".format(str))

def add_line_in_files(path, str):
    print(1)
    for root, dirs, files in os.walk(path):
        for file in files:
            file_abs = os.path.join(root, file)
            add_line(file_abs, str)
    

path = "."
str = "OK_FORMAT = True"
add_line_in_files(path, str)

add