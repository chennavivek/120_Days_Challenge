# map function

numbers = [1,2,3,4,5]
def square(number):
    return number**2
print(square(2))
# using lambda function 
print(list(map(lambda x:x**2,numbers)))

# square of a number 

def square(x):
    return x*x
numb = [1,2,3,4,5,6,7,8,9] 
print(list(map(square, numb)))

# lamba function with map
n = list(map(lambda x:x**2,numb))
print(f"print the value using the lambda function in the map:  {n}")


# Map multiple iterate 
numb1 = [1,2,3]
numb2 = [4,5,6]
result = (list(map(lambda x, y: x + y, numb1, numb2))) 
print(result)

# map() to convert a list of string to intgers 
# string to integers 
str_number = ['1','2','3','4','5']
int_number = list(map(int, str_number))
print(int_number)

# map() to convert a tuple of string to intgers 
# string to integers 
str_number = ('1','2','3','4','5')
int_number = tuple(map(int, str_number))
print(int_number)

# upper case 
words = ['apple', 'banana', 'cherry']
upper_case = list(map(str.upper,words))
print(upper_case)

# using dictionary

def get_name(person):
    return person['name'],person['age'],person['fav_color']

people=[
    {'name':'vivek', 'age':24, 'fav_color':'white'},
    {'name':'ram', 'age':27, 'fav_color':'black'}
]
result=list(map(get_name,people))
print(result)
