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
    sum=0
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
            right=curr
        sum=sum+max(left[i],curr)
    sum=sum+left[n-1]
    return sum
ratings=[1,0,2]
print(candies(ratings))

def countOfCandies(ratings):
    sum=1
    i=1
    n=len(ratings)
    up=1
    down=0
    peak=1
    while i<n:
        if ratings[i]>ratings[i-1]:
            up+=1
            peak=up
            down=0
            sum+=up
        elif ratings[i]<ratings[i-1]:
            down+=1
            up=1
            sum+=down
            if down>=peak:
                sum+=1
        else:
            up=1
            down=0
            peak=1
            sum+=1
        i+=1

    return sum
ratings=[1,2,87,87,87,2,1]
print(countOfCandies(ratings))


#trapping rain water

def trap_water(height):
    n = len(height)
    water = 0

    for i in range(n):
        max_left = max(height[:i]) if i > 0 else 0
        max_right = max(height[i+1:]) if i < n-1 else 0

        current_water = min(max_left, max_right) - height[i]
        if current_water > 0:
            water += current_water

    return water

# Example usage
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap_water(height))  # Output: 7


def findWaterLevel(height):
    n=len(height)
    left=0
    right=n-1
    maxLeft=0
    maxRight=0
    water=0
    while left<right:
        if height[left]<height[right]:
            if(height[left]>=maxLeft):
                maxLeft=height[left]
            else:
                water+=maxLeft-height[left]
            left+=1
        else:
            if(height[right]>=maxRight):
                maxRight=height[right]
            else:
                water+=maxRight-height[right]
            right=right-1
    return water
height=[2,0,1,0,2]
print(findWaterLevel(height))



#4 .Integer to roman

# Optimal
def intToRoman(num):
    int_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ""
    for value, symbol in int_to_roman:
        while num >= value:
            result += symbol
            num -= value
    return result
n=404
print(intToRoman(n))


# bruteForce
def int_to_roman(num):
    result=""
    value_to_symbol = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    if num == 0:
        return ""
    for value, symbol in value_to_symbol:
        if num >= value:
            return symbol + int_to_roman(num - value)

n=404
print(int_to_roman(n))

#5.Roman to integer
def roman_to_int(s):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    stack = []
    
    for char in s:
        current_val = roman_values[char]
        
        if stack and stack[-1] < current_val:
            stack.append(current_val - stack.pop())
        else:
            stack.append(current_val)
    
    return sum(stack)

s="CDIV"
print(roman_to_int(s))


def romanToInt(s):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    previous_val = 0
    
    for char in reversed(s):
        current_val = roman_values[char]
        
        if current_val >= previous_val:
            total += current_val
        else:
            total -= current_val
            
        previous_val = current_val
    
    return total
s="CDIV"
print(romanToInt(s))
