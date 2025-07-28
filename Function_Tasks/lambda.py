# syntax 
# lambda arguments : expression

# a simple function with 1 expression 
def addition(a,b):
    return a+b
# calling a function 
print(addition(2,4))

# argument and expression 
addition = lambda a,b : a+b  # a,b is the argument and a+b is the expression
type(addition)
print(addition(3,8))

# 
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(even(25))

# using lambda function
even1 = lambda num : num%2==0
type(even1)
print(even1(34))

# addition 
def addition(x,y,z):
    return x+y+z
print(addition(2,3,5))

# using the lambda 
addition1 = lambda x,y,z:x+y+z
print(addition1(2,3,4))

