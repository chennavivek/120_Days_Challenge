# Function with *args and **kwargs

def print_args_kwargs(*args, **kwargs):
    print('args:',args)
    print('kwargs:',kwargs)
# Test 
print_args_kwargs(1,2,3, a='apple', b= 'banana')
print_args_kwargs('hello', 'world', x=10, y=20)


