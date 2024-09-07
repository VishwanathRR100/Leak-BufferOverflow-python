dict_1 = {'name': "Vishwanath R R", "age": 19, "city": "Chennai"}

print(dict_1['name'])

dict_1["course"] = "CSE"

print(dict_1)

last_key = list(dict_1.keys())
last = last_key[len(last_key) - 1]
for key, value in dict_1.items():
    if key == last :
        print(key, value)
    else :
        print(key, value, end=" ")
for key in sorted(dict_1.keys()):
    print(key, end=" ")
for value in dict_1.values():
    print(value)

print(dict_1["name"].split())

# sets -> unique and unordered

colors = {"blue", "green", "yellow", "red"}

for color in colors:
    print(color)

color_list = list(colors)
print(color_list)

# set() will return set

dict5 = {"name": "Vishwanath R R", "age": 19, "city": "Chennai"}

del dict5["name"]
print(dict5)
del dict5
