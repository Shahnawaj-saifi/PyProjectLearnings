# unpacking tuples
# Tuple is not mutable

# Only way to make it mutable is

a, b, c = (1, 2, 3)
t = (1, 2, 3)

new_t = t + (4,)
print(new_t)

# or u can convert to list then tuple

my_list = list(t)
print(my_list)
my_list.append(5)
new_t3 = tuple(my_list)
print(new_t3)
