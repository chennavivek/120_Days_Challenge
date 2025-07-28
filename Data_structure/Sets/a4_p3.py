# set operations
set1={1,2,3,4,5}
set2={2,4,6,8,10}

# union
union_set = set1.union(set2)
print(f"Union set of set1 and set2:{union_set}")
# intersection
intersection_set = set1.intersection(set2)
print(f"Intersection of set1 and set2 :{intersection_set}")
# difference
difference_set = set1.difference(set2)
print(f"Difference of set1 and set2:{difference_set}")
# symmetric difference
sym_dif_set = set1.symmetric_difference(set2)
print(f"Symmetric difference of set1 and set2:{sym_dif_set}")


""" # we can write the above code in a more concise way using operators
set1 = set(range(1, 6))
set2 = set(range(2, 11, 2))
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Symmetric Difference: {set1 ^ set2}")
"""