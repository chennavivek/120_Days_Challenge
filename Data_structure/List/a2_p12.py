### Assignment 12: List Zipping
#Create two lists of the same length. Use the `zip` function to combine these lists into a list of tuples and print the result.

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
zipped_list = list(zip(list1, list2))
print(zipped_list)