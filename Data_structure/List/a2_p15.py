
def list_intersection(lst1, lst2):
    return [x for x in lst1 if x in lst2]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = list_intersection(list1, list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Intersection: {intersection}")