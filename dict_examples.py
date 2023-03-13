

devices1 = { "d1" : "router1", "d2" : "router2"}

print(devices1)

for word in devices1:
    print(word)

devices2 = devices1.copy()

print(f"Devices 2 is : {devices2}")
devices2["d2"] = "switch"
print(devices2)
print("Value of index d1 is: ", devices1.get("d1"))
for key, value in devices2.items():
    print(f"{key} : {value}")