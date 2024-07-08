# Ternary operator --> use for one line conditional code

a = 20
b = 30

print("a is greater b") if a > b else print("b is greater than a")
# Above code is same as below
if a > b:
    print("a is greater b")
else:
    print("b is greater than a")
