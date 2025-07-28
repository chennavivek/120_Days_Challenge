# basic concept of filter 

def even(number):
    if number%2==0:
        return True
lst = list(range(1,13)) 
print(list(filter(even,lst)))

# basic concept of filter 

def even(number):
    if number%2==0:
        return True
lst = [1,2,3,4,5,6,7,8,9,10,11,12]
print(list(filter(even,lst)))

# filter with function 
lst = [1,2,3,4,5,6,7,8,9,10,11,12]
greater_than_five = list(filter(lambda x:x>5, lst))
print(f"Prints the numbers which is greater than five {greater_than_five}")

# filter with lambda function with the multiple comditions
lst = [1,2,3,4,5,6,7,8,9,10,11,12]
even_greater_than_five = list(filter(lambda x:x>5 and x%2==0, lst))
print(f"Prints the numbers which is greater than five {even_greater_than_five}")

# Use filter() to check the age of a person, is greater then 25 or not in dictionary 
def get_name_age(person):
    return person['age']>25


people = [
    {'name':'vivek', 'age':27},
    {'name':'vk', 'age':24},
    {'name':'dhrulaxmi', 'age':25},
    {'name':'sairam', 'age':22},
    {'name':'roja', 'age':36},
    
] 
print(list(filter(get_name_age,people)))


