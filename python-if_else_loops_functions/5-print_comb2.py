#!/usr/bin/python3
for i in range(0, 100):
    if i <= 9:
        print(f"0{i}", end="")
    else:
        print(f"{i}", end="")
    if i != 99:
        print(", ", end="")
