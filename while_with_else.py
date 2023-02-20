# test if a number is prime


num = 2
i = 2

while i < num // 1:
    if num % i == 0:
        print(f"{num} is NOT prime")
        break
    i += 1
else: # this is else for while statement
    print(f"{num} is prime")

    