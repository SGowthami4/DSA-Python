##1 .Remove duplicates in-place from sorted array
## Brute force  
# def remove(arr):
#     ans_arr=[]
#     ans_arr.append(arr[0])
#     for i in range(1,len(arr)):
#         if arr[i]!=arr[i-1]:
#             ans_arr.append(arr[i])
#     return ans_arr
# arr=[1,1,1,2,2,3,3]
# print(len(remove(arr)))  
print("===============================================================================================")
#space complexity-O(N)   time-complexity-O(N)

# def removeDuplicates(nums):
#     ans=[]
#     index=0
#     if(nums):
#         ans.append(nums[0])
#         for i in range(1,len(nums)):
#             if(nums[i]!=nums[i-1]):
#                 ans.append(nums[i])
#         for i in ans:
#             nums[index]=i
#             index+=1
#         return nums
    
# arr1=[-1,0,0,0,0,3,3]
# print(removeDuplicates(arr1))
print("====================================================================================================================")
# Optimal solution -two pointer approach
# def remove_duplicates(arr):
#     j=1
#     for i in range(1,len(arr)):
#         if arr[i]!=arr[i-1]:
#             arr[j]=arr[i]
#             j+=1
#     return j
# arr=[0,0,1,1,2,3,3,4]
# print(remove_duplicates(arr))

print("=======================================================================================================================")

#2. Remove Element
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# def removeElement(arr2,k):
#     j=0
#     for i in range(len(arr2)):
#         if arr2[i]!=k:
#             arr2[j]=arr2[i]
#             j+=1
#     return j

# arr2=[2,2,3,3]
# k=2
# print(removeElement(arr2,k))
print("===============================================================================================================")
##Best Time to Buy and Sell Stock II
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
def maxProfit(prices):
    ans=0
    min_prices=0
    for i in range(1,len(prices)):
        if(prices[i]<prices[min_prices]):
            min_prices=i
        else:
            ans += (prices[i]-prices[min_prices])
            min_prices+=1
    return ans
arr=[7,1,5,3,6,4]
arr1=[1,2,3,4,5]
print(maxProfit(arr))
print(maxProfit(arr1))
print("=====================================================================")