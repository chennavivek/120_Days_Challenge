# function decorator

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Excuting function')
        result= func(*args, **kwargs)
        print('Function executed')
        return result
    return wrapper
@my_decorator
def sum_list(lst):
    return sum(lst)
#test 
print(sum_list([1,2,3,4,5]))
