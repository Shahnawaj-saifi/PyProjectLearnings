my_list = [1, 2, 3, 4]

#
# my_temp_list = []
#
# for i in list:
#     temp = i * 2
#     my_temp_list.append(temp)
#
# print(my_temp_list)

def double_f(num):
    return num ** 2


double_list = list(map(double_f, my_list))
print(double_list)
