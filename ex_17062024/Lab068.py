# Leap Year

year = 2028

(year % 4 == 0)
(year % 100 != 0)
(year % 400 == 0)

if (year % 400 == 0) and (year % 100 != 0) or (year % 4 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

