num = 71

for i in range(2, num):
    if num % i == 0:
        print(f"{num} is NOT prime")
        break

else:
    print(f"{num} is prime")