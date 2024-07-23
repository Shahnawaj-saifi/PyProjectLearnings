# Triangle Classifier

side1 = 3
side2 = 2
side3 = 3

if(side1 == side2 == side3):
    print("Equilateral")
elif(side1 == side2 or side2 == side3 or side3 == side1):
    print("Isoceles")
else:
    print("Scalene")