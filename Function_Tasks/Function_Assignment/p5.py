# Variable length arguments

def variable_number(*args):
    product = 1
    for num in args:
        product *= num 
    return product
# test
print(variable_number(2,3,4))
