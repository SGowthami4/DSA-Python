# Second Largest Element
def second_large(arr):
    n=len(arr)
    if n<2:
        return -1
    first=second=float('-inf')
    for num in arr:
        if num>first:
            second=first
            first=num
        elif num>second and num!=first:
            second=num
    if second==float('-inf'):
        return -1
    else:
        return second

arr=[10,2,12,35,22,36,34]
print(second_large(arr))

# 2.Move all zeros to end

# Brute Force Approach
def moveZeroes(arr):
    temp=[0]*len(arr)
    j=0
    for i in range(len(arr)):
        if(arr[i]!=0):
            temp[j]=arr[i]
            j+=1
    while j<len(arr):
        temp[j]=0
        j+=1
    return temp

arr=[1,0,3,0,2,4,0,5,0]
print(moveZeroes(arr))

# T.C-O(n) ,S.C-O(n)


def pushZerosToEnd(arr):
    # count of non-zero elements
    count=0
    # If the element is non-zero,replace the element at
    # index 'count' with this element and increment count
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1

     # Now all non-zero elements have been shifted to
     # the front , make all elements 0 fom count to end 
    while count<len(arr):
        arr[count]=0
        count+=1
    return arr   
arr=[1,0,3,0,2,4,0,5,0]
print(pushZerosToEnd(arr))
# T.c-O(2n),S.c-O(1)

#Better Approach
def pushZeroes(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[count]=arr[count],arr[i]
            count+=1


arr=[1,0,3,0,2,4,0,5,0]
pushZeroes(arr)
print(arr)
# T.C-O(n),S.C-O(1)

# 3. Reverse an Array
