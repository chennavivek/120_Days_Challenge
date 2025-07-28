# removing elements from sets 

s = set(range(1, 6))
print(f"Original set: {s}")
s.pop()  # Remove and return an arbitrary element from the set
print(f"Set after pop: {s}")


## 

s = set(range(1, 6))
while s:  # Continue until the set is empty
    s.pop()  # Remove and return an arbitrary element from the set
    print(f"Set after pop: {s}")