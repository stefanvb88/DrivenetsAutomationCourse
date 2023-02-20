for i in range(11):
    for j in range(i, 11): ##when using start "i" will not iterate duplicate results
        result = i * j
        print(f"{i} x {j} equals  {result}")
    print() # prints a new line