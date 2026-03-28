#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    for i in my_list:
        if i not in unique:
            unique.append(i)
    result = 0
    for k in unique:
        result += k

    return result
