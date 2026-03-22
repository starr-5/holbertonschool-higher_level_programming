for i in range (0, 100):
    num1 = i//10
    num2 = i%10
    if num1 < num2:
        print("{:02d}".format(i), end=", ")
    if i == 89:
        print("{:02d}".format(i), end="\n")
