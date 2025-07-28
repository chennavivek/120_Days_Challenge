# dict filtering
d = {i: i**2 for i in range(1,11)}
even_key = {k: v for k,v in d.items() if k % 2 == 0}
print(even_key)

