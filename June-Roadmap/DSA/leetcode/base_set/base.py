### mini problem 1: count how many times a value appears
def trackValue(arr, val):
    count = 0
    for i in arr:
        if i == val:
            count += 1
    return count
print(trackValue([1,2,3,4,4,56,7,6,7], 7))

### mini problem 2: creating a new array excluding a value; input: [3, 2, 2, 3], 3 output: [2, 2]
"""
def value(nums, val):
    return [num for num in nums if num != val]
print(value([3, 2, 2, 3], 3))

def value2(arr, value):
    return [a for a in arr if a != value]
print(value2([3, 2, 2, 3], 2))

def valueMain(nums, value):
    return [num for num in nums if num != value]
print(valueMain([3, 2, 2, 3], 3)) 

def remove_val_new_array(nums, val):
    result = []
    for num in nums:
        if num != val:
            result.append(num)
    return result               
print(remove_val_new_array([3, 2, 2, 3], 3))    
"""


