


list1 = list(range(0, 100))
print(list1)

print(any(list1)) # at least one is true
print(all(list1)) # all should be true  # 0 is false from all the elements so the result is False

nums = [0, 2 ,4, 12, 32, 99, 102]


all_even = all(num / 2 == 0 for num in nums)
any_odd = any(num % 2 for num in nums)
print(f"all even = {all_even}")
print(f"at least one odd = {any_odd}")
