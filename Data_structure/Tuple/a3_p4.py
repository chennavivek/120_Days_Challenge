nested_tuple = (
    [1,2,3],
    [4,5,6],
    [6,7,8]
)
print(f"nested_tuple :{nested_tuple}")
for row in nested_tuple:
    print(row)
print(f"element at secongd row and third column: {nested_tuple[1][2]}")