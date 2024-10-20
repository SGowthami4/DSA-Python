# 1)Jump Game:
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

#Optimal solution
def canJump(nums):
    n=len(nums)
    reachable=0
    for i in range(n):
        if(reachable<i):
            return False
        reachable=max(reachable,i+nums[i])
    return True

def canReach(nums1):
    lastreach=len(nums1)-1
    j=len(nums1)-1
    for i in nums1:
        if(j+nums1[j]>=lastreach):
            lastreach=j
        j=j-1
    if(lastreach==0):
        return True
    return False


def jump(nums1):
    if(len(nums1)==0):
        return True
    jumpable=[False for i in range(len(nums1))]
    jumpable[0]=True
    for i in range(len(nums1)): 
        if(jumpable[i]==False):
            return False
        reachable=min(len(nums1),i+nums1[i]+1)
        for j in range(i+1,reachable):
            jumpable[j]=True
    return True

nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]
print(jump(nums2))
# print(canJump(nums2))
print("=====================================================================================================")
# 2)Jump Game II

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2

def minJumps( arr, n):
        if n<=1:
            return 0
            
        maxReach=arr[0]
        step=arr[0]
        jump=1
        for i in range(1,n):
            if i==n-1:
                return jump
                     
            maxReach=max(maxReach,i+arr[i])
            step-=1
            if step==0:
                jump+=1
                if i>=maxReach:
                    return -1
                step=maxReach-i
        return -1

arr1=[2,3,1,1,4]
# print(minJumps(arr1,len(arr1)))

def minJumps(arr):
    n=len(arr)
    jumps=[float('inf')]*n
    jumps[0]=0
    for i in range(n):
        for j in range(1,arr[i]+1):
            if i+j<n:
                jumps[i+j]=min(jumps[i+j],jumps[i]+1)
    return jumps[-1]
    


   


arr2=[2,3,1,1,4]
print(minJumps(arr2))

print("===============================================================================================================")

# 3)H-Index

# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

# Example 1:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:

# Input: citations = [1,3,1]
# Output: 1

#Brute Force 
def h_index(citations):
    n=len(citations)
    h_index=0
    for i in range(n+1):
        count=sum(1 for val in citations if val>=i)
        if count>=i:
            h_index=i
    return h_index

def h_index(citations):
    citations.sort(reverse=True)
    h_index=0
    for i,citation in enumerate(citations):
        if citation>=i+1:
            h_index=i+1
        else:
            break
    return h_index
citations = [1,3,1]
print("h_index:",h_index(citations))


print("===================================================================================================================")

# 4)Insert Delete GetRandom O(1):
# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

 

# Example 1:

# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


import random 
class RandomizedSet:
    def __init__(self):
        self.elements=[]
    def insert(self,val):
        if val in self.elements:
            return False
        self.elements.append(val)
        return True
    def remove(self,val):
        if val not in self.elements:
            return False
        self.elements.remove(val)
        return True
    def getRandom(self):
        return random.choice(self.elements)

# randomized_set=RandomizedSet()
# randomized_set.insert(1) 
# randomized_set.remove(2)
# randomized_set.insert(2)
# randomized_set.getRandom()
# randomized_set.remove(1)
# randomized_set.insert(2)
# randomized_set.getRandom()
def getResult(operations,values):
    result=[]
    randomized_set=None

    for i,operation in enumerate(operations):
        if operation=="RandomizedSet":
           randomized_set=RandomizedSet()
           result.append("null")
        elif operation=="insert":
            result.append(randomized_set.insert(values[i][0]))
        elif operation=="remove":
            result.append(randomized_set.remove(values[i][0]))
        elif operation=="getRandom":
            result.append(randomized_set.getRandom())

    return result

operations=["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
values=[[], [1], [2], [2], [], [1], [2], []]
ans=getResult(operations,values)
print(ans)

#Optimal approach
import random
class RandomSet:
    def __init__(self):
        self.list=[]
        self.dict={}
    
    def insert(self,val):
        if val in self.dict:
            return False
        self.dict[val]=len(self.list)
        self.list.append(val)
        return True
    def remove(self,val):
        if val not in self.dict:
            return False
        index=self.dict[val]
        last_element=self.list[-1]
        self.list[index]=last_element
        self.dict[last_element]=index
        self.list.pop()
        del self.dict[val]
        return True
    def getRandom(self):
        return random.choice(self.list)
    
def getResult(operations,values):
    result=[]
    random_set=None

    for i,operation in enumerate(operations):
        if operation=="RandomSet":
            random_set=RandomSet()
            result.append("null")
        elif operation=="insert":
            result.append(random_set.insert(values[i][0]))
        elif operation=="remove":
            result.append(random_set.remove(values[i][0]))
        elif operation=="getRandom":
            result.append(random_set.getRandom())

    return result

operations=["RandomSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
values=[[], [1], [2], [2], [], [1], [2], []]
ans=getResult(operations,values)
# print(ans)



print("=======================================================================================================")

# 5)Product of array except itself:

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Brute force
def Product(arr):
    n=len(arr)
    result=[]
    for i in range(n):
        product=1
        for j in range(n):
            if i!=j:
                product *=arr[j]
        result.append(product)
    return result
arr=[1,2,3,4]
print(Product(arr))

# Optimal approach

def productExceptSelf(arr):
    n=len(arr)
    result=[1]*n
    left_product=1
    for i in range(n):
        result[i]=left_product
        left_product *=arr[i]
    right_product=1
    for i in range(n-1,-1,-1):
        result[i] *=right_product
        right_product*=arr[i]
    return result        

arr1=[-1,1,0,-3,3]
print(productExceptSelf(arr1))