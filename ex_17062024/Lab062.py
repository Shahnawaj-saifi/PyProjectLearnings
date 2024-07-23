# * args - any number of arguments

def sum_three(a= 5, b= 6, c= 9):
    return a + b + c


# ------------------result = sum_three()
result1 = sum_three(1, 2, 3)
result2 = sum_three(10, 2)
result3 = sum_three(10, 2, 3)
result4 = sum_three(22, 3)
result5 = sum_three(1, 2, 30)
print(result4, result5, result1, result2, result3)
