#!/usr/bin/python3
def binary_search(arr,low,high,x):
    #Index of middle element

    if high >= low:
        mid = ( low + high ) // 2

        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            return binary_search(arr,low,mid-1,x)
        elif x > arr[mid]:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1

array1=[1,3,5,7,12,15,22]
search_value=15
index=binary_search(array1,0,len(array1)-1,search_value)
print("Value is found at ",index)
