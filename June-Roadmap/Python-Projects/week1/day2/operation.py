#1 Array insertion
arr = [1, 3, 5, 7, 8, 10]
print(arr.copy())
arr.insert(2, 3) # insert 3 at the index 2 So, first parameter is index and the second one is the value
print(arr)

#2. array deletion concept: Removing element and shifting remaining elements.
arr2 = [1, 45, 67, 78, 33, 78]
print(arr2.copy())
arr2.remove(78) # removes the first occurrence of 78
print(arr2)
"""
or we can use del keyword # that will delete element of specific index
del arr2[4] 
print(arr2)
"""

#3. Array Searching a. Linear Search (used when the array is unsorted)
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1
    
print(linear_search([1, 23, 45, 65, 7], 7))    

### removing duplicates
def removingDuplicates(arr):
    if not arr:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1
print(removingDuplicates([11,2,23,11,34,334,1,2,3,3,2,2,2,4]))


