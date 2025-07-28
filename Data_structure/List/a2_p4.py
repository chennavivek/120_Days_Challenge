# P4 List Comprehensions
# Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.

square = [num**2 for num in range(1,11)]
print(f"The first 10 positive integer of a list is:{square}")
