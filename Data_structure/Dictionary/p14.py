# counting with dictionary 

def count_chars(s):
    count_dict ={}
    for char in s:
        count_dict[char]= count_dict.get(char,0)
    return count_dict
string = "hello vivek"
print(count_chars(string))


# Corrected Version (to actually count characters):
# To fix this, you should increment the count for each character:

def count_chars(s):
    count_dict = {}
    for char in s:
        count_dict[char] = count_dict.get(char, 0) + 1  # Increment the count
    return count_dict

string = "hello vivek"
print(count_chars(string))