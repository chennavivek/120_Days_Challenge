inventory = ['apple', 'banana', 'cherry', "grapes"]

inventory.append('orange')
inventory.remove('banana')

item = "orange"
if item in inventory:
    print(f"{item} are in stock")
else:
    print(f"{item} ate out of stock")

print("Inventory List")
for item in inventory:
    print(f"-{item}")
