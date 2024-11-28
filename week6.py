# Week 5 --DSA

# 1) Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


def isPalindrome(string):
        string="".join([string[i] for i in range(len(string)) if (string[i].isalnum())])
        l, r = 0, len(string) - 1
        while l < r:
            if string[l].lower() != string[r].lower():
                 return False
            l += 1
            r -= 1
        return True
s="A man, a plan, a canal: Panama"
print(isPalindrome(s))


def isPalindrome(s):
        l=0
        r=len(s)-1
        while l<r:
            while l<r and not(s[l].isalnum()):
                l+=1
            while l<r and not(s[r].isalnum()):
                r-=1
            if s[l].lower() != s[r].lower():
                 return False
            l += 1
            r -= 1
        return True


s=".,"
print(isPalindrome(s))

# 2)Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

def isSubsequence(s,t):
    index_in_t = 0
    for char in s:
        found = False
        while index_in_t < len(t):
            if t[index_in_t] == char:
                found = True
                index_in_t += 1
                break
            index_in_t += 1
        if not found:
            return False
    return True

s = "acb"
t = "ahbgdc"
print(isSubsequence(s,t))

def isSubsequence(s, t):
    s_ptr = 0
    t_ptr = 0
    
    while s_ptr < len(s) and t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        t_ptr += 1
    
    return s_ptr == len(s)

s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))

def isSubsequence(s,t):
    if s == "":
        return True
    if t == "":
        return False
    
    cont = 0
    for char in t:
        if char == s[cont]:
            cont += 1
        if cont == len(s):
            return True

    return False    

s = "acb"
t = "ahbgdc"
print(isSubsequence(s, t))    



#Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

def twoSum(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
    return None

numbers=[2,3,4]
target=6
print(twoSum(numbers,target))

def find(nums,target):
    l,r=0,len(nums)-1
    while l<r:
        curr_sum=nums[l]+nums[r]
        if curr_sum==target:
            return [l+1,r+1]
        elif curr_sum<target:
            l+=1
        else:
            r-=1
    return None

nums=[2,7,11,15]
target=9
print(find(nums,target))


# Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
def waterLevel(heights):
    max_water=0
    n=len(heights)
    for i in range(n):
        for j in range(i+1,n):
            height=min(heights[i],heights[j])
            width=j-i
            water=height*width
        max_water=max(max_water,water)
    return max_water

heights = [1,8,6,2,5,4,8,3,7]
print(waterLevel(heights))

def solve(heights):
    max_water=0
    l=0
    r=len(heights)-1
    while l<=r:
        curr_water=min(heights[l],heights[r])*(r-l)
        if curr_water>max_water:
            max_water=curr_water
        if heights[l]<heights[r]:
            l=l+1
        else:
            r=r-1
    return max_water

heights = [1,8,6,2,5,4,8,3,7]
print(solve(heights))

def maxArea(height):
    l, r =  0,  len(height) - 1
    maxWater = 0

    while l < r:
        lowerHeight = min(height[l], height[r])
        water = lowerHeight *(r -l)
        maxWater = max(maxWater, water)
            
        while l<r and height[r] <= lowerHeight:
            r -= 1
        while l<r and height[l] <= lowerHeight:
            l += 1
    return maxWater
    
heights = [1,8,6,2,5,4,8,3,7]
print(maxArea(heights))

## 3 Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

def findSum(nums):
    nums.sort()
    n=len(nums)
    result=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    result.add((nums[i],nums[j],nums[k]))
    return [list(i) for i in result]

nums = [0,1,1]
print(findSum(nums))     

def threeSum(nums):
    res=[]
    nums.sort()
    for i,a in enumerate(nums):
        if i>0 and a==nums[i-1]:
            continue
        l,r=i+1,len(nums)-1
        while l<r:
            threeSum=a+nums[l]+nums[r]
            if threeSum>0:
                r-=1
            elif threeSum<0:
                l+=1
            else:
                res.append([a,nums[l],nums[r]])
                l+=1
                while nums[l]==nums[l-1] and l<r:
                    l+=1
    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))