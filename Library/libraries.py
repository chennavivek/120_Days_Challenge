# 
import array

ary = array.array('i',[1,2,3,4,5])
print(ary)

# random

import random
print(random.randint(1,10))
print(random.choice(['vivek', 'sonu', 'roja', 'ramesh']))

# common library we use is OS that is file and directory access 
import os 
print(os.getcwd())

# can make a directory 
# os.mkdir('test_directory')

# To create a file, you can use the built-in open() function with mode 'w' or 'x'
with open('example_file.txt', 'w') as f:
    f.write('This is a new file.')

# high level operations on files and collection of files 
import shutil
print(shutil.copyfile('example_file.txt','destination.txt'))

# Data serialization
import json
data = {'name': 'vivek', 'age':24}  # dic to str 
json_str = json.dumps(data)
print(json_str)
print(type(json_str))
parsed_data = json.loads(json_str)   # str to dic 
print(parsed_data)
print(type(parsed_data))

# csv file 

import csv

with open('example.csv', mode = 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['dhru', 24])
with open('example.csv',mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# datetime 

from datetime import datetime, timedelta
now = datetime.now()
print(now)
yesterday = now-timedelta(days=1)
print(yesterday)

# time 
import time
print(time.time())
time.sleep(2)
print(time.time())

# regular expresion
import re
pattern = r'\d+'
text = 'There are 123 apples'
match = re.search(pattern,text)
print(match.group())
