# Higher order function 
def higher_order_function(func, lst):
    return [func(x) for x in lst]
print(higher_order_function(lambda x : x ** 2, [1,2,3,4,5]))
print(higher_order_function(lambda x : x +1, [1,2,3,4,5]))
