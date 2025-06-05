### GIVEN two arrays, return an array that contains elements
# present in both
def intersectionTwoArrays(arr1, arr2):
    intersectionArray = []
    for element in arr2:
        if element in arr1:
            intersectionArray.append(element)
    return intersectionArray

print(intersectionTwoArrays([1, 2, 3, 4, 2], [2, 2]))   
            
