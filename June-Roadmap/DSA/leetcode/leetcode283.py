def moveZero(arr):
    pos = 0
    for num in arr:
        if num != 0:
            arr[pos] = num
            pos += 1
    while pos < len(arr):
        arr[pos] = 0
        pos += 1
    return arr    
print(moveZero([0,2,2,3,0,0,0,234,7]))                
