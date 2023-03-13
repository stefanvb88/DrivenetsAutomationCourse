tpl1 = (1,2,3,4,5)
tpl2 = (6,7,8,9,10)

try:
    tpl1[0] = 100
except TypeError as e:
    print(f"TypeError: {e}")

print(f"However you can slice tuples")
print(f"tpl1[0:2]: {tpl1[0:2]}")

#what is i want to change the value of the first element of the tuple?

tpl3 = (100, *tpl1[1:0])  #this is called tuple unpacking
print(f"tpl3: {tpl3}")
tpl4 = (100,) + tpl1[1:] # this is called tuple concatenation
print(f"tpl: {tpl3}")

print(dir(tuple))