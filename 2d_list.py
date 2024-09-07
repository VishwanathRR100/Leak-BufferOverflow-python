# arr = arr2 -> partial copy
# arr = arr2[:] -> shallow copy only applies to 1D array
# arr = arr2.copy() -> shallow copy

# for deep copy

import copy

tn = ["Chennai","Salem","Madurai"]
kl = ["Cochin,Thiruvananthapuram"]
kn = ["Bangalore","Mangalore"]

India = [tn,kl,kn]

Indian_states = copy.deepcopy(India)

India[0][1] = "Coimbatore"

print(India[0][1])
print(Indian_states[0][1])