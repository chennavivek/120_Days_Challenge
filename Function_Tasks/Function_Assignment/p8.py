# Recursive function

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
# test 
print(factorial(5))
print(factorial(3))
    