# P3: List Slicing
# Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in P1.
list_positive_integers = list(range(1,21))
print(list_positive_integers)
print(f"The first 5 elements from the P1 list: {list_positive_integers[:5]}")
print(f"The last 5 elements from the P1 list: {list_positive_integers[-5:]}")
print(f"The elements from the index 5 to 15 list: {list_positive_integers[5:15]}")
