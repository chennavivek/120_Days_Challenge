## crete a new file directory 
import os

path = 'package'
if not os.path.exists(path):
    os.mkdir(path)
    print(f"Directory '{path}' created")
else:
    print(f"Directory '{path}' already exists")

# Listing files and directory 
items = os.listdir('.')
print(items)

## joining path

dir_name = "folder"
file_name = "file.txt"
full_path = os.path.join(dir_name,file_name)
print(full_path)

###
dir_name = "folder"
file_name = "file.txt"
full_path = os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)

## crete a new file directory 

path = 'example1.txt'
if os.path.exists(path):
    print(f"Directory '{path}' already exists")
else:
    print(f"Directory '{path}' does not exists")

# checking if a path or dir is present or not in the file 

path = "sample.txt"
if os.path.isfile(path):
    print(f"The path {path} is a file")
elif os.path.isdir(path):
    print(f"The path {path} is a directory")
else:
    print(f"The path {path} is neither a path nor a directory")

## Getting a absolute path 
relative_path = 'sample.txt'
absolute_path = os.path.abspath(relative_path)
print(absolute_path)