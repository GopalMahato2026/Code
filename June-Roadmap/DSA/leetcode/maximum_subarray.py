## leetcode 53 Maximum subarray
def maxiSubarray(nums):
    current_sum = 0
    max_sum = float("-inf")
    
    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum
print(maxiSubarray([12,2,34,-23,234,32]))    

