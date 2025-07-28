# calculate the total cost of the shopping cart

# define a shopping cart as a list of dictionaries 

shopping_cart = [
    {'item':'apple',  'price_per_unit':1,   'quantity': 5},
    {'item':'tomato', 'price_per_unit':2.5, 'quantity':5},
    {'item':'sprit',  'price_per_unit':3,   'quantity': 5},
    {'item':'salt',   'price_per_unit':2.5, 'quantity': 5}
] 

# function to calculate the total cost 
def calculate_total_cost(cart):
    total_cost = 0
    for product in cart:
        cost = product['quantity']*product['price_per_unit']
        total_cost += cost
    return total_cost

# calculate and print the total cost in the cart 
total = calculate_total_cost(shopping_cart) 
print(f"Total cost of the shopping cart is: ${total:.2f}")


# # Define a shopping cart as a list of dictionaries
# shopping_cart = [
#     {"item": "Apple", "quantity": 3, "price_per_unit": 0.5},
#     {"item": "Bread", "quantity": 2, "price_per_unit": 2.0},
#     {"item": "Milk", "quantity": 1, "price_per_unit": 1.5},
#     {"item": "Eggs", "quantity": 12, "price_per_unit": 0.1}
# ]

# # Function to calculate total cost
# def calculate_total_cost(cart):
#     total_cost = 0
#     for product in cart:
#         cost = product["quantity"] * product["price_per_unit"]
#         total_cost += cost
#     return total_cost

# # Calculate and print the total cost
# total = calculate_total_cost(shopping_cart)
# print(f"Total cost of the shopping cart is: ${total:.2f}")
