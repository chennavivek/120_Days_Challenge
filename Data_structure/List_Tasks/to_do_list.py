# To do list 
to_do_list = ["Buy Groceries", "Clean the house", "Pays Bills"]
to_do_list.append("Laundry") # adding the task in the list 
to_do_list.append("Gym") # adding the task in the list
to_do_list.remove("Laundry") # Remove completed task from the to do list 

if "Pays Bills" in to_do_list:
    print("Don't forget to pay the bills")
print("To Do List remainig")
for task in to_do_list:
    print(f"-{task}")

