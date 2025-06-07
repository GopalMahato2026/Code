## Leetcode 1 Two sum
# i was given an array and a target my job is to find the two indexes that are equal to the target i mean The addition Two indexes are equal to the target
def twoSum(nums, target):
    prevDict = {}
    for i, num in enumerate(nums):
        diff = target - num # i'll check difference of each value from the target
        if diff in prevDict: #if diff is found that means we return the index of diff and the current index that will add up to the target
            return [prevDict[diff], i]
        # if not found i can add the value and its index to the dict
        prevDict[num] = i
print(twoSum([1,2,3,4,5,5,6], 6))   
print("---" * 16)
##maximum subarray
def maximumSubarray(arr):
    current_sum = 0
    max_sum = 0
    for i in arr:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum
print(maximumSubarray([5, 4, -1, 7, 8]))

print("---" * 16)
def moveZero(nums):
    pos = 0
    for num in range(len(nums)):
        if nums[num] != 0:
            nums[pos] = nums[num]
            pos += 1
        
    # filling remaining position to zero
    for num in range(pos, len(nums)):
        nums[num] = 0
    return nums
num1 =[12,0, 0, 82, 89, 7, 0, 5]
print(f"Original: {num1} | Using moveZero function: {moveZero(num1)}")

print("---" * 16)

# best time to buy and sell stock
def bestProfit(prices):
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit

print(bestProfit([12,22,2,234,3,5,6]))

print("---" * 16)
#217. Contains Duplicates
# I was given a integer array nums, return true if any value appears at least twice in the array. and return false if every element is distinct.

def checkDuplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
           return True
        seen.add(num)   
            
    return False
print(checkDuplicates([1,1,2,2]))
print(checkDuplicates([1,7,2,17]))

print("---" * 16)
# - Intersection of Two Arrays II (LC #350)
"""
I was given two integer arrays nums1 and nums2, I need to return an array of their intersection. Each element in the result must appear as must as it shows in both arrays and you may return the result in any order.
"""
def countElement(nums1, nums2):
    myDict = {}
    for number in nums1:
        if number in myDict:
            myDict[number] += 1
        else:
            myDict[number] = 1
    result = []
    for number in nums2:
        if number in myDict and myDict[number] > 0:
            result.append(number)
            myDict[number] -= 1
    return result        

print(countElement([1, 2, 2, 7, 1], [2, 7,  2]))
# it must return 1: 0, 22: 3, 7: 3, 17: 3 

print("---" * 16)
# Valid Anagram (LC #242)
# i was give a two strings s and t, i need to return true if t is an anagram of s, ans false otherwise.
def countDict(value):
    myDict = {}
    for num in value.lower():
        if num in myDict:
            myDict[num] += 1
        else:
            myDict[num] = 1
    return myDict        
def isAnagram(s, t):    
    s_count = countDict(s)
    t_count = countDict(t)
    return s_count == t_count

print(isAnagram("Gopal", "opalg"))    
print(isAnagram("ram", "rom"))

print("|","-_" * 25,"|")
print("-------------Reverse string section----------------")
#Reverse String (LC #344) 
"""
writing a function that reverse a string. The input string is given as an array of characters s.
I need to must do this by modifying the input array in-place with extra memory.
example input: s = ["h", "e", "l", "l","o"]

"""

def reverseString(s):
    start = 0
    end = len(s) - 1
    
    while start < end:
        s[start], s[end] = s[end], s[start]
        start, end = start + 1, end - 1
    return s    

print(reverseString(["h", "e", "l", "l","o"]))

print("---" * 16)
#- Rotate Array (LC #189)
"""
I was given an array nums, i need to rotate the array to the right by k steps, where k is non-negative 
Example input: nums = [1,2,3,4,5,6,7], k = 3
Example Output: [5, 6, 7, 1, 2, 3, 4]
"""
def convertReverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1
    return nums

def rotateArray(nums, k):
    k = k % len(nums)
    n = len(nums)
    convertReverse(nums, 0, n -1)
    convertReverse(nums, 0, k - 1)
    convertReverse(nums, k, n - 1)
    return nums
print(rotateArray([1,2,3,4,5,6,7], 3))   

print("---" * 16)

# Plus One (LC #66)
"""
Example input: [1, 2, 3]
Example Output: [1, 2, 4]
"""
def plusOne(digits):    
    
    for digit in range(len(digits) -1 , -1, -1):
        if digits[digit] < 9:
            digits[digit] += 1
            return digits
        digits[digit] = 0    
    return [1] + digits    
  
print(plusOne([9, 9, 9]))

print("---" * 16)

##Remove Element (LC #27) 
"""
input: nums = [0, 1, 2, 2, 3, 0, 4, 2] , val = 2
output: 5, nums = [0, 1, 4, 0, 3]
"""

def removeVal(nums, val):
    pos = 0
    
    for num in range(len(nums)):
        if nums[num] != val:
            nums[pos] = nums[num]
            pos += 1

    return pos 
print(removeVal([0, 1, 2, 2, 3, 0, 4, 2], 2))  

print("---" * 16)

def isPalindromeNum(x):
    s = str(x)
    print(s[::-1])
        
    return s == s[::-1]
print(isPalindromeNum(123))    

print("---" * 16)
#Valid Palindrome (LC #125)
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""
def isPalindrome(x):
    cleanVersion = ""
    for char in x:
        if char.isalnum():
            cleanVersion += char.lower()
    return cleanVersion == cleanVersion[::-1]        
print(isPalindrome("A man, a plan, a canal: Panama")) 

def isPalindromeV2(s):
    chars = []
    for char in s:
        if char.isalnum():
            chars.append(char.lower())
    return chars == chars[::-1]
    
print(isPalindromeV2("A man, a plan, a canal: Panama"))    
        





            
    
