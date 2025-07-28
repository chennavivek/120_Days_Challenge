# syntax 
def function_name(parameters):
    """docstring"""
    # function body 
    return
 
# If a function is even or odd ?
number = 57
if number % 2 == 0:
    print(f"It is a even number")
else:
    print(f"It is a odd number")

# 
def even_or_odd(number):
    """Returns 'even' if the number is even, 'odd' otherwise."""
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# calling a func
# result = even_or_odd(57)
print(f"57 is an {even_or_odd(57)} number")

# function with multiple parameters
# add of two numbers 

def add(a,b):
    return a+b
print(add(2,7))

# default parameters 
def greet(name):
    print(f"HI {name}")
greet("VIVEK")

#
def greet(name = 'VIVEK'):
    print(f"HI {name}")
greet()

# variable with argument
# positional and keywords arguments 

# postional argument 
def print_number(*args):
    for number in args:
        print(number)
print_number(1,2,3,4,5,'vk')

# keyword argument
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_details(name ='vivek', age = 24, location = 'usa')    

# postional argument & keyword argument
def print_details(*args, **kwargs):
    for val in args:
        print(f"Positional : {val}")
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_details(1,2,3,4,5,'vk',name ='vivek', age = 24, location = 'usa')

# return function

def multiply(a,b):
    return a * b

print(multiply(3,2))

# return multiple parameters

def multiply(a,b):
    return a * b, a

print(multiply(3,2))

