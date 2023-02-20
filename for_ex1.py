import time
start_time = time.time()


a = "text5text"
list = [1,2,3,4]

#for char in a:
#    print(char)

#for item in list:
#    print(item)


s = 0

for i in range(0,10):
    s += i
print(s)
print(f"it took {time.time() - start_time}")