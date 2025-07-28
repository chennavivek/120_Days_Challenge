### Assignment 8: List of Dictionaries

# Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. 
# Sort the list of dictionaries by the 'score' in descending order and print the sorted list.

# student = {key : value, key : value} each dictionary represents a student
students = [
    {'name': 'Vk', 'score': 88},
    {'name': 'Dl', 'score': 72},
    {'name': 'Uk', 'score': 95},
    {'name': 'Aj', 'score': 65},
    {'name': 'fd', 'score': 78}
]
sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)
print("Sorted students by score in descending order:")
for student in sorted_students:
    print(student)
"""
This line does several important things:

sorted() is Python's built-in function that returns a new sorted list

The first argument students is the list we want to sort

key=lambda x: x['score'] defines how to sort:

lambda creates an anonymous function

For each student dictionary x, we extract the 'score' value

The sorting will be based on these score values

reverse=True makes the sort descending (high to low) instead of ascending
"""
