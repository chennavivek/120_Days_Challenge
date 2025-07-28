# Empty Dictionary 
empty_dict ={}
print(empty_dict)
print(type(empty_dict))

# using a dict()
empty_dict2= dict()
print(empty_dict2)
print(type(empty_dict2))

# Dictionary with values
student = {"name": "vivek", "age": 24, "is_student": True} # key value (name , age , else ) should be unique not repeated or duplicated
print(student)
print(type(student))

student = {"name": "vivek", "age": 24, "is_student": True} # key value (name , age , else ) should be unique not repeated or duplicated
print(student)

# Accessing values in a dictionary
print(student["age"])  # Accessing the value associated with the key 'age'
print(student.get("name")) # Using the get method to access the value associated with the key 'name'
print(student.get("last_name"))

# Using get method with a default value
print(student.get("last_name", "Not Found"))  # If 'last_name' key is not found, it returns "Not Found"

# modifying a dictionary
# dictionary are mutable you can add, delete or update the values
# updated
student["age"]=25 # Changing the value associated with the key 'age'
print(student)

# Added 
student["last_name"]="Chenna"
print(student)

#Deleting
del student["is_student"]  # Deleting the key 'is_student'
print(student)

# Dictionary methods
# keys() method returns a view object that displays a list of all the keys in the dictionary
print(student.keys())    # get all keys
print(student.values()) # get all values
print(student.items())  # get all key-value pairs

#shallow copy
student_copy = student
print(student_copy)
print(student) 
student_copy["age"] = 30  # Modifying the copy will also modify the original dictionary
print(student)  # Both will show the updated age
print(student_copy)
# shallow copy creates a new reference to the same dictionary object, so changes in one will reflect in the other.
student_copy = student.copy()  # This creates a shallow copy of the dictionary
print(student_copy)
student_copy["age"] = 35  # Modifying the copy will not affect the original dictionary
print(student)  # Original dictionary remains unchanged
print(student_copy)

# Iterating through a dictionary
# you can use a for loop to iterate through the keys, values, or key-value pairs of a dictionary
# Iterating through keys, values, and items in a dictionary
for key in student.keys():
    print(key)  # Prints each key in the dictionary

for value in student.values():
    print(value)  # Prints each value in the dictionary

for key,value in student.items():
    print(f"{key}:{value}")  # Prints each key-value (item) pair as a tuple

# Nested dictionaries
# A dictionary can contain other dictionaries as values, allowing for complex data structures
nested_dict ={
    "student1": {"name": "vivek", "age": 24, "last_name":"chenna"},
    "student2": {"name": "john", "age": 22, "last_name":"doe"},
    "student3": {"name": "alice", "age": 23, "last_name":"smith"},
    "student4": {"name": "bob", "age": 21, "last_name":"brown"},

}
print(nested_dict)  

# Accessing values in a nested dictionary
print(nested_dict["student1"]["name"])  # Accessing the name of student1
print(nested_dict["student2"]["age"])   # Accessing the age of student2
print(nested_dict["student3"]["last_name"])  # Accessing the last name of student3
print(nested_dict['student1']["last_name"])  # Accessing the last name of student1

# iterating through a nested dictionary
for student_key, student_info in nested_dict.items():
    print(f"{student_key}: {student_info}")  # Prints each student key and their information
    for key, value in student_info.items():
        print(f"{key}: {value}")  # Prints each key-value pair for the student

# dictionary comprehension
square = {x: x**2 for x in range(1, 11)}
print(square)  # Prints a dictionary with numbers as keys and their squares as values

# Example of dictionary comprehension with a condition
even_square ={x:x**2 for x in range(1,11) if x%2==0}
print(even_square)  # Prints a dictionary with even numbers as keys and their squares as values

# Example 

numbers = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
print(frequency)
