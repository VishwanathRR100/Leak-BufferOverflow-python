def bubble_sort(arr):
    for i in range(1,len(arr)):
        sorted = False
        for j in range(0,len(arr)-i):
            if(arr[j]>arr[j+1]):
                print(f'{i}=>{j}')
                (arr[j],arr[j+1]) = (arr[j+1],arr[j])
                sorted = True
        if(sorted == False):
            break

    return arr

print(bubble_sort([72,243,1,7,144,32,25,92,90]))
