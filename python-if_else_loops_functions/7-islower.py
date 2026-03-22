#!/usr/bin/python3
def uppercase(str):
    a = ''
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            a += chr(ord(i) - 32)
        else:
            a += i
    print("{}".format(a))
