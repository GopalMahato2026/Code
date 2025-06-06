##merging two sorted arrays
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
"""
# test 1
"""
Write a function that merges [1,3,5] and [2,4,6] into [1,2,3,4,5,6].

Try this first (no in-place required).
"""
"""
def merge(arr1, arr2):
    return sorted(arr1 + arr2)

print(merge([1,3,5],[2,4,6]))  
"""
# test2 lets try this without using sorted method
"""

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

"""
"""
def mergeVersion2(arr):
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    arr = arr1 + arr2
    n = len(arr)
    for passes in range(n - 1):
        for j in range(0, (n - 1) - passes):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
  
print(mergeVersion2([2,3,21,3,2,34,6])) 

"""

## version3
def mergeArray(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    ##adding remaining element
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result[::-1] 
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

print(mergeArray(arr1, arr2))


    
    
