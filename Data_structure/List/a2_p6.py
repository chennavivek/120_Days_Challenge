# Assignment 6: List Methods
# Create a list of random numbers and sort it in ascending and descending order.
# Remove the duplicates from the list and print the modified list.

import random

random_numbers = [random.randint(1, 20) for random_number in range(15)]
# random_numbers = [random.randint(1, 20) for _ in range(15)]
print(random_numbers) # the 15 random numbers from the list btw the 1 to 20 

# sort it in ascending and descending order

ascending_numbers = sorted(random_numbers)
print(f"the ascending order of the list: {ascending_numbers}")

descending_numbers = sorted(random_numbers, reverse=True)
print(f"the descending order ofnthe list: {descending_numbers}")

# remove duplicate values

duplicate_value = list(set(random_numbers))
print(f"after removing the duplicate values from the list: {random_numbers}")