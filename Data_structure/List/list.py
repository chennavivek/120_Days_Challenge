# how the list are work or perform.
# list are mutable 

#ex
friends = ["vivek", "dhrulaxmi", 34.9, 32, True, "roja"] # this is list
print(friends[3]) # printing the value 

#ex
a = "vivek"
print(a[1])

# we can change the value in the list 
#ex
friends = ["vivek", "dhrulaxmi", 34.9, 32, True, "roja"] 
friends[0] = "my_love" # so we can change the value in the list but we cant change the value in the string because str is immutable
print(friends[0])

print(friends) # printing the list after changing the list value 
print(friends[1:4]) # printing the value from the 1 to 4 but 4 is not included.

friends.append("iam_in_love_with_DL")  # added iam_in_love_with_DL in the list using append method 
print(friends)   

l1 = [1,2,3,32,4,54,67,8]  
l1.sort() # using the sort() func we can arrange the list in the order 
print(l1)

# reverse() func
l1.reverse() # it will run the list in the reverse 
print(l1)

# like this we have so many func 
# insert()

l1.insert(3,4) # insert the value 4 in the place of 3 index
print(l1) 
# [67, 54, 32, 4, 8, 4, 3, 2, 1] the output loook like this because we have useing the list of reverse func so for that reason we are getting the 4 value after 32 because it was using the -1 -2 -3 sciling

value = l1.pop(3) # pop the value from the list 
print(value)
print(l1)

# remove the value from the list
print(l1)
l1.remove(1) # the value 1 was removed not the 1 index value 
print(l1)

print(friends)

# pop method

p = friends.pop()
print(p)
print(friends)

# iterating over list 
for frds in friends:
    print(frds)


# iterating in index 

for index,frds in enumerate(friends):
    print(index,frds)

# list comprehension 
# basic syntax

number = [num**2 for num in range(10)]
print(number)

# list comprehension with conditional 
lst = []
for i in range(10):
   if i%2 == 0:
      lst.append(i)
print(lst)      

# conditional statement 
# even_number = [num for num in range(10) if num%2 == 0]
# print(even_number)
even_number = [i for i in range(10) if i%2 == 0]
print(even_number)

# nested list comprehension
list_1 = [1,2,3,4,5]
list_2 = ['a','b','c','d','e']
two_lists = [[i,j] for i in list_1 for j in list_2] # printing the two list with using nested function
print(two_lists)