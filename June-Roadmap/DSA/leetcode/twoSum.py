#leetcode 1
def twoSum(arr, target):
    preDict = {}
    for i, n in enumerate(arr):
        diff = target - n
        if diff in preDict:
            return [preDict[diff], i]
        preDict[n] = i
print(twoSum([1, 2, 3, 4, 5], 6))

