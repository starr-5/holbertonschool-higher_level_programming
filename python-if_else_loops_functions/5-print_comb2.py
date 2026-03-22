#!/usr/bin/python3
for i in range(0, 100):
    if i <= 9:
        num = f"0{i}"
    else:
        num = f"{i}"
    
    if i == 99:
        print(num, end="")
    else:
        print(num, end=",")