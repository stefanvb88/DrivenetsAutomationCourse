a = list(range(101))
print(1)

#pay attention slice returns a copy of the list
print(a[10:20])# 10 to 19
print(a[:30]) #0-29
print(a[80:]) #80 - 100
print(a[20:40:4]) # 20, 24, 28, 32, 34, 36
print(a[::-2]) # 100, 98, 96 ...