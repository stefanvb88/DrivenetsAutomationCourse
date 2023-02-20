# "infinite" while with escape mechanism

s = 0
while True:
    try:
        num = int(input("Please gice me a number:(0 to quit) "))
        if num == 0:
            break
        s += num
    except ValueError:
        print("That is not a valid number")
        continue
    print(f"Intermidiate sum so for is {s}")

    # code here
    # escape mechanism that breaks


print(s)
