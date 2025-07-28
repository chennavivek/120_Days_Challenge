# Flattening a Nested List
# Write a function that takes a nested list and flattens it into a single list.
# print the original and flattened lists.

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def flatten_list(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return flat_list
flattened = flatten_list(nested_list)
print("Original nested list:")
print(nested_list)
print("Flattened list:")
print(flattened)