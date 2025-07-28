### Assignment 14: List Rotation
#Write a function that rotates a list by n positions. Print the original and rotated lists.

def roate_list(lst, n):
    n = n % len(lst)  # Handle cases where n is larger than the list length
    return lst[-n:] + lst[:-n]
original_list = [1, 2, 3, 4, 5]
n = 2
rotated_list = roate_list(original_list, n)
print("Original list:", original_list)
print("Rotated list:", rotated_list)    