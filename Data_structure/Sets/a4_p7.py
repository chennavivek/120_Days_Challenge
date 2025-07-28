# subsets and superset

set1 = {1,2,3,4,5}  # (range(1,6))
set2 = {1,2,3} # (range(1,4))
subset_set = set2.issubset(set1) # Check if set2 is a subset of set1
print(f"Is set2 is a subset of set1? {subset_set}")
superset_set = set1.issuperset(set2)
print(f"Is set1 is a superset of set2? {superset_set}")  # it does not contain all the elements of set2

# another way to check subset and superset

range(1,6)
range(1,4)
print(set2.issubset(set1))  # True
print(set1.issuperset(set2))  # True