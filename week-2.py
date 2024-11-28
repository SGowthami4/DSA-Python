# 1) Remove Duplicates from Sorted Array II
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

#Brute Force 
def removeDuplicates(nums):
    ans=[]
    i=0
    index=0
    if (len(nums)<=2):
        return len(nums)
    else:
        ans.append(nums[0])
        ans.append(nums[1])
        for j in range(2,len(nums)):
            if (nums[j]!=nums[j-2]):
                ans.append(nums[j])
        for k in range(len(ans)):
            nums[index]=ans[k]
            index+=1
        return index

nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))

#Optimal solution

def remove_Duplicates(nums1):
    i=0
    for e in nums1:
        if i==0  or i==1 or nums1[i-2]!=e:
            nums1[i]=e
            i+=1
    return i
nums1 = [0,0,1,1,1,1,2,3,3]


nums2=[0,0,1,1,1,2,3,3]
print("remove duplicates from sorted array 2:",remove_Duplicates(nums2))

print("============================================================================================")
#2)Majority Element
# Brute force

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def Majority(nums):
    ans=0
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                count+=1
        if count>len(nums)//2:
            ans=nums[i]
    return ans




nums=[3,3,4]
print(Majority(nums))


# def majority(num):
#     m=dict()
#     ans=0
#     for i in nums:
#         if i in m:
#             m[i]+=1
#         else:
#             m[i]=1
#     for j in nums:
#         if m[j]>len(nums)//2:
#             ans=j
#     return ans

def majorityElement(nums):

        # Moore's algorithm
        count=0
        res=0
        for i in range(len(nums)):
            if count==0:
                res=nums[i]
            if nums[i]!=res:
                count=count-1
            else:
                count=count+1
        return res

nums = [6,5,5]
print(majorityElement(nums))
# print(majority(nums))

print("=================================================================================================")

# 3)Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotate(nums,k):
    temp=nums[:len(nums)-k]
    for i in range(len(nums)-k,len(nums)):
        nums[i-k-1]=nums[i]
    for i in range(len(temp)):
        nums[k+i]=temp[i]
    return nums
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums,k))

# 4)Best Time to Buy and Sell Stock 
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 
def solve(n, prices):
    max_profit=0
    min_till=prices[0]
    for i in range(1,n):
        curr=prices[i]
        profit=curr-min_till
        if profit>max_profit:
            max_profit=profit
        if min_till>curr:
            min_till=curr
    return max_profit
prices= [7,1,5,3,6,4]
n=6
print(solve(n,prices))

def bestTimeToBuyAndSell(n,prices):
    max_profit=0
    max_till=prices[n-1]
    for i in range(n-2,-1,-1):
        curr=prices[i]
        profit=max_till-curr
        if profit>max_profit:
            max_profit=profit
        if max_till<curr:
            max_till=curr
    return max_profit

prices= [7,1,5,3,6,4]
n=6
print(bestTimeToBuyAndSell(n,prices))


#5)Best Time to Buy and Sell Stock II
def Stock(arr):
    profit=[]
    ans=0
    min_price=0
    for i in range(1,len(arr)):
        if arr[i]<arr[min_price]:
            min_price=i
        else:
            ans += (arr[i]-arr[min_price])
            min_price +=1
            
    for i in profit:
        ans+=i
    return ans
            
def stock(arr):
    ans=0
    min_price=0
    for i in range(1,len(arr)):
        if(arr[i]<arr[min_price]):
            min_price=i
        else:
            check=arr[i]-arr[min_price]
            ans+=check
            min_price+=1
    return ans
            
prices = [1,2,3,4,5]
print(Stock(prices))
print(stock(prices))