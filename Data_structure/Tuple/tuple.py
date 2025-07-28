# tuple
#empty tuple 
tpl = tuple()
print(type(tpl))


# printing a single value 
a = (1,) # if you won't use the comma then it return the int instead of tuple lets try that 
t = (type(a))
print(t) # output <class 'tuple'>

a = (1) # if you won't use the comma then it return the int instead of tuple lets try that 
t = (type(a))
print(t)  # output <class 'int'>

#type conversion 
# list into tuple
l = tuple([1,2,3,4,5])
print(l) 

# mixed data types
mix_tuples = (1, "dhrulaxmi", "vivek", 1.432, True)
print( mix_tuples)

# a = (1,2,3,4,5,6,7,8,9)
# a[0] = 3
# # it will not change because it is immutable 

# find the length of a tuple 
a = (1,2,3,4,5,6,7,8,9)
l = len(a)
print(l)

# concatenation of tuples
numbers = (1, 2, 3, 4, 5)
letters = ("a", "b", "c", "d", "e")
concatenated_tuple = numbers + letters
print(concatenated_tuple)

# slicing a tuple
sliced_tuple = concatenated_tuple[2:5]  # slicing from index 2
print(sliced_tuple)

# tuple methods 
# count method
tpl = (1, 2, 3, 1, 2, 1)
print(tpl.count(1))  # Output: 3, counts how many times 1 appears in the tuple
print(tpl.index(2))  # Output: 1, returns the index of the first occurrence of 2

# packing tuple  
my_tuple = 1, "vk", 3.14  # packing values into a tuple
print(my_tuple)  # Output: (1, 'vk', 3.14)

# unpacking the tuple
a,b,c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3 

# unpacking with *

numbers = (1, 2, 3, 4, 5)
first, *middle, last=numbers
print(first)
print(middle)
print(last)

# output 
# 1
# [2, 3, 4]
# 5