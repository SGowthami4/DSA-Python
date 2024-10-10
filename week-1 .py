##1 .Remove duplicates in-place from sorted array
## Brute force   with updating original arr
def remove(arr):
    ans_arr=[]
    ans_arr.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            ans_arr.append(arr[i])
    return ans_arr
arr=[1,1,1,2,2,3,3]
print(len(remove(arr)))
#space complexity-O(N)   time-complexity-O(N)

def removeDuplicates(nums):
    ans=[]
    index=0
    if(nums):
        ans.append(nums[0])
        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]):
                ans.append(nums[i])
        for i in ans:
            nums[index]=i
            index+=1
        return nums
    
arr1=[-1,0,0,0,0,3,3]
print(removeDuplicates(arr1))

# Optimal solution -two pointer approach
def remove_duplicates(arr):
    j=1
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            arr[j]=arr[i]
            j+=1
    return j
arr=[0,0,1,1,2,3,3,4]
print(remove_duplicates(arr))

