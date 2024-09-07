# our implementation :
# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         i_val = i
#         j=i-1
#         while(j>=0):
#             val_j = abs(j)
#             if(arr[val_j]>arr[i_val]):
#                 (arr[val_j],arr[i_val])=(arr[i_val],arr[val_j])
#                 i_val = val_j
#             elif(arr[val_j]<arr[i_val]):
#                 break
#             j = j-1
#     return arr

def insertion_sort(arr):
    for i in range(1,len(arr)):
        i_val = arr[i]
        j=i-1
        while(j>=0 and i_val<arr[j]):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = i_val
    return arr

print(insertion_sort([1,2,34,5,56,21,122]))