# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8

num = 2
square = num ** 2
cube = num ** 3
print("The square of", num, "is", square)
print("The Cube of", num, "is", cube)


# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

# creating function for comparing two numbers
def compare_numbers(num1, num2):
    if num1 > num2:

        return "The first number is greater than the second number."

    elif num1 < num2:

        return "The first number is less than the second number."

    else:

        return "The first number is equal to the second number."


# Output

num1 = float(input("Enter the first number and press Enter Key:  "))

num2 = float(input("Enter the second number and press Enter Key: "))

result = compare_numbers(num1, num2)

print(result)
