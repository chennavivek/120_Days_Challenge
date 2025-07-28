# set and list conversion 
st = set(range(1,6)) # Create a set from a range of numbers
lst = list(st) # Convert set to list
lst.append(6) # Adding an element to the list
st = set(lst) # Convert list back to set
print(lst) # Output the list


