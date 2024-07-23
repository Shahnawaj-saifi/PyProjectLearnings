# Function
def say_hello(name):
    print("Hello", name)


# say_hello("Shahnawaj")

result = say_hello("Shahnawaj")
print(result)


def say_hello_name(name="Roma"):
    print("Hello", name)

say_hello_name()
say_hello_name("Amit")
say_hello_name(name="Sumit")

def sum_return(a,b): # argument with return type
    return a + b

result = sum_return(a=3, b=5)
print(result)
