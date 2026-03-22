#!/usr/bin/python3
def uppercase(str):
    a = ''
    for i in str:
        if i >= chr(ord('a')) and i <= chr(ord('z')):
            i = chr(ord(i)-32)
            a = a + i
        else:
            a = a + i
    return a
