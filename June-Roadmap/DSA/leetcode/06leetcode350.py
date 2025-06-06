### GIVEN two arrays, return an array that contains elements
# present in both
"""
def intersectionTwoArrays(arr1, arr2):
    intersectionArray = []
    for element in arr2:
        if element in arr1:
            intersectionArray.append(element)
    return intersectionArray

print(intersectionTwoArrays([1, 2, 3, 4, 2], [2, 2]))   
"""
def countValue(arr1, arr2):
    myDict = {}
    for num in arr1:
        if num in myDict:
            myDict[num] += 1
        else:
            myDict[num] = 1
    
    result = []
    for num in arr2:
        if num in myDict and myDict[num] > 0:
            result.append(num)
            myDict[num] -= 1
    return result        
        
arr1 = [1, 2, 2, 2]
arr2 = [2, 2]
print(countValue(arr1, arr2))

    



