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
    # j=2
    # for i in range(2,len(nums1)):
    #     if (nums1[i]!=nums1[i-2]):
    #         nums1[j]=nums1[i]
    #         j+=1
    #     else:
    #         j=i
    # return nums1[:j]
    i=0
    for e in nums1:
        if i==0  or i==1 or nums1[i-2]!=e:
            nums1[i]=e
            i+=1
    return i
# nums1 = [0,0,1,1,1,1,2,3,3]


nums2=[0,0,1,1,1,2,3,3]
print(remove_Duplicates(nums2))