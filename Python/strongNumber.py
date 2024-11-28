# def fact(s):
#     ans=1
#     if s==1:
#         return 1
#     else:
#         ans=s*fact(s-1)
#     return ans
# def isStrong(n):
#     sum1=0
#     for i in (str(n)):
#         sum1+=fact(int(i))
#     return sum1==n

# print(isStrong(145))
def fact(s):
    ans=1
    for i in range(s,0,-1):
        ans*=i
    return ans

def isStrong(n):
    sum1=0
    for i in (str(n)):
        sum1+=fact(int(i))
    return sum1==n

print(isStrong(40585))

# T.C-O(d)  -no.of digits in number
# S.C-O(1)

# Efficient compared to the above

def isStrong(n):
    # Precompute factorials of digits 0-9
    factorial = [1] * 10
    for i in range(2, 10):
        factorial[i] = factorial[i - 1] * i

    # Check if n is a strong number
    sum1 = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum1 += factorial[digit]
        if sum1 > n:  # Early exit if sum exceeds the number
            return False
        temp //= 10

    return sum1 == n

print(isStrong(40585))  # True

# T.C-O(d)
# T.C-O(1)