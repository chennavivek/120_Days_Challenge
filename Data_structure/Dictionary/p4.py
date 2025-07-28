# iterating through a dictionary
d = {i: i**2 for i in range(1, 11)}
print(d)
for key, value in d.items():
    print(f"{key}:{value}")