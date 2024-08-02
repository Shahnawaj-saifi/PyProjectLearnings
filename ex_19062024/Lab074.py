# number = [1,2,3]
#
# def do_something(my_list):
#     my_list.append(34)
#     my_list[0] = 10
#     return my_list
#
# a = do_something(number)
# print(a)

number = [1, 2, 3]


def do_something(number):
    number[0] = 10
    number[2] = 6
    number.append(34)
    return number


a = do_something(number)
print(a)
