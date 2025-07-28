# dic key and value transformation

d = {i : i**2 for i in range(1,6)}
swapped_dict = {v:k for k, v in d.items()}
print(swapped_dict)