# merging dictionaries

d1 = {x:x**2 for x in range(1,6)}
d2 = {x:x**2 for x in range(6,11)}
merged_dict ={**d1, **d2} 
print(merged_dict)


# another method to do the same thing
d1 = {i: i**2 for i in range(1, 6)}
d2 = {i: i**2 for i in range(6, 11)}
d1.update(d2)
print(d1)