# Nested Function
def outer_function(x,y):
    def inner_function(a,b):
        return a*b
    return inner_function(x,y)
# test 
print(outer_function(2,3))
