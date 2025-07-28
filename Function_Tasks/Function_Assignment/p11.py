# Filter Function
# find the all odd numbers from the list 
numbers = [1,2,3,4,5,6,7,8,9]
odd_numbers = list(filter(lambda x : x % 2 != 0, numbers))
print(f"all the odd numbers from the list: {odd_numbers}")

# find the all even numbers from the list 
numbers = [1,2,3,4,5,6,7,8,9]
even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(f"all the even numbers from the list: {even_numbers}")
