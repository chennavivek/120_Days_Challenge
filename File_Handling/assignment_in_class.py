# Read a text file and count the number of lines, words, and characters.

file_path = '/Users/vivekchenna/Library/Mobile Documents/com~apple~CloudDocs/DataAnalyst/120_Days_challenge/File_Handling/sample.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

num_lines = len(lines)
num_words = sum(len(line.split()) for line in lines)
num_chars = sum(len(line) for line in lines)

print(f"Lines: {num_lines}")
print(f"Words: {num_words}")
print(f"Characters: {num_chars}")


#writing and then reading a file 
with open('sample.txt', 'w+') as file:
    file.write("Hello vivek\n")
    file.write("This is a new line\n")
# Move the cursor to the beginning 
    file.seek(0)

# Read the content of the file 
    content = file.read()
    print(content)
