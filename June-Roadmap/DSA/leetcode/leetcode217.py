def containsDuplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True    
        seen.add(num)
    return False
print(containsDuplicates([1,2,2,2,34,5,5,5]))
    
