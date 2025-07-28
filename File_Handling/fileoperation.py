# read a whole file
file_path = '/Users/vivekchenna/Library/Mobile Documents/com~apple~CloudDocs/DataAnalyst/120_Days_challenge/File_Handling/exe.txt'
with open(file_path, 'r') as file:
    content = file.read()
    print(content)

# read a file line by line 
with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())

# read a file line by line 
with open(file_path, 'w') as file:
    print(file.write('Hello vivek \n'))
    print(file.write('this is new line'))

# write a file witout overwriting
with open(file_path, 'a') as file:
    print(file.write("\nAppend operation taking place"))

# writing a list of lines to file 
lines = ['\nfirst line\n','second line\n','third line\n' ]
with open(file_path, 'a') as file:
    file.writelines(lines)

# binary files

data = b'\x00\x01\x02\x03\x04'
with open('example.bin', 'wb') as file:
    print(file.write(data))

with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)

# write the function from a source text file and write to a destination file 

file_path = '/Users/vivekchenna/Library/Mobile Documents/com~apple~CloudDocs/DataAnalyst/120_Days_challenge/File_Handling/exe.txt'
with open(file_path, 'r') as source_file:
    content = source_file.read()
with open('destination_path', 'w') as destination_file:
    destination_file.write(content)


# Example usage:
# copy_file('source.txt', 'destination.txt')

