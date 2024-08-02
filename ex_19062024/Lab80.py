# List is collection of items (Duplicate allowed)
my_list = [1, 2, 4]
my_list2 = [1, 2, "Shahnawaj", 1.1]

# Indexing
print("Element at index 0:", my_list[0])

# Changing an element
my_list[1] = 20
print("List after changing element at index 1:", my_list)

# append()
my_list.append(7)
print("append", my_list)

# extend() --> extending list item
my_list.extend([8])
print("extend", my_list)

# insertion
my_list.insert(3,"a")
print("insert", my_list)

# remove
my_list.remove("a")
print("remove", my_list)

# copy
my_copy_list = my_list.copy()
print(my_copy_list)

