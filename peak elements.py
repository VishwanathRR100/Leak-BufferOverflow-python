arr = [5,2,1,21,78,2,76,3,75,60,89]
peak = []
for i in range(0,len(arr)):
    if i==0:
        if arr[i] > arr[i+1]:
            peak.append(arr[i])
    elif i==len(arr)-1:
        if arr[i] > arr[i-1]:
            peak.append(arr[i])
    else:
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            peak.append(arr[i])

print(peak)

