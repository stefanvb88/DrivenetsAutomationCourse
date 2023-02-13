try:
    a = int(input("Give me a number: "))
    if (a > 0) and (a < 10):
        print(f"{a} is a posivive number")
        print(f"{a} is less than 10")
    elif a< 0:
        print(f"{a} is a negative number")
    else:
        print(f"{a} was not of the above")
except ValueError:
    print("this is not a number")




