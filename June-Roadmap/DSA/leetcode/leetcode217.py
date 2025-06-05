def containsDuplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True    
        seen.add(num)
    return False
print(containsDuplicates([1,2,2,2,34,5,5,5]))
    
    
    
    
    
    
    
    
 #practicing this problem one more time
 ## what this problem says, "You are given an integers. check if any value appear at least twice in the array
 
def checkDuplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
print(checkDuplicates([1,2,2,2,3,7]))    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
