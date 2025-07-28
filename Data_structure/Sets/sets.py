# create a set 
set = {1, 2, 3, 4, 5}
print(set)
print(type(set))

my_set = ([1, 2, 3, 4, 5])
print(type(my_set))
                                      
# create a set with duplicate values
duplicate_set = {1, 2, 3, 4, 4, 3, 5}
print(duplicate_set)

# Basic operations on sets
# add
duplicate_set.add(6)
print(duplicate_set)

#remove 
duplicate_set.remove(6)
print(duplicate_set)

# pop 
removed_element = duplicate_set.pop()
print(f"Removed element: {removed_element}")
print(duplicate_set)

# clear
duplicate_set.clear()
print(duplicate_set)

# set membership
set = {1, 2, 3, 4, 5}
print(4 in set)  # True / False
print(6 in set)  # False / True
print(2 in set)  # True / False

#Mathematical operations on sets
set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8,9,10}
# union
union_set = set1.union(set2)
print(f"Union:{union_set}")

# intersetion
intersection_set =set1.intersection(set2)
print(f"Intersection: {intersection_set}")

# intersection update
set1.intersection_update(set2)
print(f"Intersection Update: {set1}")

# difference
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
difference_set = set1.difference(set2)
print(f"Difference (set1 - set2): {difference_set}")

# difference update
set2.difference(set1)
print(set2)

# symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2) # all the common common elements are removed
print(f"Symmetric Difference: {symmetric_difference_set}")

# set methods 
set1 = {1,2,3}
set2 ={3,4,5}
# issubset
is_subset = set1.issubset(set2)
print(f"Is set1 a subset of set2?{is_subset}")

# issuperset
is_superset = set1.issuperset(set2)
print(f"Is set1 a superset of set2?{is_superset}")  # it does not contain all the elements of set2

# converting list to set
# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers = set(numbers)
# print(unique_numbers) 

#counting unique words in a sentence
# sentence = "he hi this is vivek i know i will be a good programmer"
# words= sentence.split()
# unique_words = set(words)
# print(f"Unique words: {unique_words}")
# print(f"number of unique words: {len(unique_words)}")