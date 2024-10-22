# 1. Gas Station
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

 

# Example 1:

# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.

# Example 2:

# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1

#brute force1
def canCompleteCircuit(gas,cost):
    n=len(gas)
    for start in range(n):
        fuel=0
        valid=True
        for i in range(n):
            station=(start+i)%n
            fuel+=gas[station]-cost[station]
            if fuel<0:
                valid=False
                break

        if valid:
            return start
    return -1


gas=[1,2,3,4,5]
cost=[3,4,5,1,2]
print(canCompleteCircuit(gas,cost))



#Optimal solution
def canComplete(gas,cost):
    current=0
    start=0
    total_fuel=total_cost=0
    for i in range(len(gas)):
        total_fuel+=gas[i]
        total_cost+=cost[i]
    if total_fuel<total_cost:
        return -1
    for i in range(len(gas)):
        current+=gas[i]-cost[i]
        if current<0:
            start=i+1
            current=0
    return start
gas = [2,3,4]
cost = [3,4,3]
print(canComplete(gas,cost))

print("======================================================================================================")

#Candy
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

#     Each child must have at least one candy.
#     Children with a higher rating get more candies than their neighbors.

# Return the minimum number of candies you need to have to distribute the candies to the children.
# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.

 
def Candy(ratings):
    n=len(ratings)
    left=[0]*n
    right=[0]*n
    left[0]=1
    right[n-1]=1
    for i in range(1,n):
        if ratings[i]>ratings[i-1]:
            left[i]=left[i-1]+1
        else:
            left[i]=1
    for i in range(n-2,-1,-1):
        if ratings[i]>ratings[i+1]:
            right[i]=right[i+1]+1 
        else:
            right[i]=1
    sum=0
    for i in range(n):
        sum=sum+max(left[i],right[i])
    return sum

ratings=[1,0,2]
print(Candy(ratings))

def candies(ratings):
    n=len(ratings)
    left=[0]*n
    left[0]=1
    sum=max(1,left[n-1])
    for i in range(1,n):
        if ratings[i]>ratings[i-1]:
            left[i]=left[i-1]+1
        else:
            left[i]=1
    curr=1
    right=1
    for i in range(n-2,-1,-1):
        if ratings[i]>ratings[i+1]:
            curr=right+1
            right=curr
        else:
            curr=1
        sum=sum+max(left[i],curr)
    return sum
ratings=[1,0,2]
print(candies(ratings))


