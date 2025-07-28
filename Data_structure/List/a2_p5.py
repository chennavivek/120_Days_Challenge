# P5: Filtering Lists
# Create a new list containing only the even numbers from the list created in P1 using a list comprehension. Print the new list.
list_positive_integers = list(range(1,21))
print(list_positive_integers) 

even_numbers = [num for num in list_positive_integers if num % 2 == 0]
# concept 
# a = [expression for in iteration condition] 
# for to find the even numbers we have to right the if condition _____%2 == 0
print(even_numbers)