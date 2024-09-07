# variable length arguement , we can give any number of arguments and it converts to tuple

def total(*args):
    total = 0
    for i in args:
        total += i
    return total

# here kwargs are cnverted to dictionary , kwargs are used for keyword declaration o paramaters

print(total(4, 5, 6, 12))

def print_addr(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value}')

print_addr(door_no = "93",street_name="KK nagar",addr_line = "Velachery")