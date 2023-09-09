#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_if_even = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            check_if_even.append(True)
        else:
            check_if_even.append(False)

    return (check_if_even)
