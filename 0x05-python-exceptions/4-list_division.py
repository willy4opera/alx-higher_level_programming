#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    nw_lst = []
    for num in range(0, list_length):
        try:
            divide = my_list_1[num] / my_list_2[num]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            nw_lst.append(divide)
    return (nw_lst)
