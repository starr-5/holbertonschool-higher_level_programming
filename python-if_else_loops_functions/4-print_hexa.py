#!/usr/bin/python3
for i in range(0, 99):
    a = i
    result = ''
    digits = "0123456789abcdef"
    if i == 0:
        result = '0'
    while i > 0:
        remainder = i % 16
        result = digits[remainder] + result
        i = i//16
    print("{} = 0x{}".format(a, result))
