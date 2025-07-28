# Dictionary methods 
d = {i: i**2 for i in range(1, 11)}
print(d)

# add a new key-value pair
d[11] = 121
print(f"After adding a new key-value pair:{d}")
d.pop(1)
print(f"After removing a key-value pair 1:{d}")
# # remove a key-value pair
# del d[1]
# print(f"After removing a key-value pair:{d}")
