# function documentation
def doc_string(x,y):
    """ 
    This function takes two integers and returns their sum>

    parameters:
    x (int): The first integer.
    y (int): The second integer.

    Returns:
    int:The sum of the two integers.
    """
    return x + y
print(doc_string.__doc__)