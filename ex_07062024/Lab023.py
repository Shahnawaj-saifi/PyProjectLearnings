# List  --> Shopping list --> array
# milk, poha, bread, butter
# Add items
# Remove
# update
# view
# Exit

shopping_list = ["Milk", "Bread", "Butter", "Poha"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[3])

shopping_list.append("curd")
shopping_list.insert(3,"jam") # insert anywhere as per given index
print(shopping_list)
shopping_list.extend(["pulses","wheat"]) # add multiple item in the list
print(shopping_list)

shopping_list.pop()  # delete last item = pop()
shopping_list.sort()
print(shopping_list)

# list/array can contain different data type

my_list = ['Shahnawaj', '2.14', '230', True]
print(type(my_list))