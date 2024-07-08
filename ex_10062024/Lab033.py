# program --> calculate the area of circle.
# input --> radius
# output --> result
import math

# formula --> pi r **2

radius = float(input("Enter Radius\n"))
# print(math.pi)
area = math.pi * (math.pow(radius, 2))
print("Area of circle is", area)
