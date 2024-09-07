arr = [1,-3,5,-13,45,-9,7]

for i in range(0,len(arr)):
    if(arr[i]<0):
        neg = arr.pop(i)
        arr.append(neg)

print(arr)