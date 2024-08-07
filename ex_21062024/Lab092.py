t = ("The", "Academy", "The", "Testing")
print(set(t))

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7}
my_set1 = set3.intersection(set4)
print(my_set1)

# differences

my_set3 = set3.difference(set4)
print(my_set3)
