###
"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

"""
def reverse_list(arr, start, end):    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start, end = start + 1, end - 1
    return arr

def rotateRight(arr, k):
    start = 0
    end = len(arr) - 1
    k = k % len(arr)
    reverse_list(arr, start, end) ## [7,6,5,4,3,2,1]
    reverse_list(arr, start, k - 1) ## [5, 6, 7, 4, 3, 2, 1]
    reverse_list(arr, k, end)   ## [5, 6, 7, 1, 2, 3, 4] 
    return arr
print(rotateRight([1,2,3,4,5,6,7], 3))    



"""
Input: [10, 20, 30, 40, 50, 60], k = 2  
Output: [50, 60, 10, 20, 30, 40]
"""
  
    
