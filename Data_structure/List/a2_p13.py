### Assignment 13: List Reversal
#Write a function that takes a list and returns a new list with the elements in reverse order. Print the original and reversed lists.


def reverse_list(lst):
    return lst[::-1]
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print("Original list:", original_list)
print("Reversed list:", reversed_list)