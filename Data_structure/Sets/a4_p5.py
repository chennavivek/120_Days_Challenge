# filtering sets
positive_integer = set(range(1, 11))  # Set of positive integers from 1 to 10
print(f"Positive intergers: {positive_integer}")
even_numbers = {x for x in positive_integer if x % 2 == 0}
print(f"Even numbers: {even_numbers}")
