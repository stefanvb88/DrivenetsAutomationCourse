import math
import random

a = int("123")
print(a)
print(id(a))
print(min([1, 3, -99, 100]))

#math example
print(math.sin(math.radians(30)))

print("random".center(50, "-"))
print (random.random())
print(random.randint(1, 100))
print(random.randint(1, 2))
print(random.choice(["apple", "banana", "kiwi"]))

s = 0
for i in range(10):
    s += random.randint(1,10)
print(s)