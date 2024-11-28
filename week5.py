# 1.Length of Last Word

# Optimal solution

def lastWordLength(s):
    i=len(s)-1
    count=0
    while i>=0 and s[i]==" ":
        i=i-1
    while i>=0 and s[i]!=" ":
        count+=1
        i=i-1
    return count

s="Hello World"
print(lastWordLength(s))

#Brute force
def last_word_length(s):
    words=s.split(" ")
    i=len(words)-1
    for j in range(i,-1,-1):
         if words[j]!="":
             return len(words[j])


s="   fly me   to   the moon  "
print(last_word_length(s))


#2.Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

#Brute-force
def longestCommonPrefix(s):
    if not s:
        return ""
    def common_prefix(left,right):
        min_length=min(len(left),len(right))
        for i in range(min_length):
            if left[i]!=right[i]:
                return left[:i]
        return left[:min_length]
    def divide_and_conquer(s,left,right):
        if left==right:
            return s[left]
        mid=(left+right)//2
        lcp_left=divide_and_conquer(s,left,mid)
        lcp_right=divide_and_conquer(s,mid+1,right)
        return common_prefix(lcp_left,lcp_right)
    return divide_and_conquer(s,0,len(s)-1)

s=["flower","flow","flight"]
print(longestCommonPrefix(s))

#Optimal solution
def longest_common_prefix(s):
    if not s:
        return ""
    for i in range(len(s[0])):
        char=s[0][i]
        for str in s:
            if i>=len(s) or str[i]!=char:
                return s[0][:i]
    return s[0]
s=["flower","flow","flight"]
print(longest_common_prefix(s))



#3. Reversing words in a string

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
def reverse(s):
    words=s.split()
    st=[]
    for word in words:
        st.append(word)
    reversed_words=[]
    while st:
        reversed_words.append(st.pop())
    return " ".join(reversed_words)

    
s = "a good   example"
print(reverse(s))  

def reverse_word(s):
    words=s.split()
    reversed_words=words[::-1]
    return " ".join(reversed_words)

s = "a good   example"
print(reverse_word(s))

def reversed_words_in_place(s):
    chars=list(s)
    def reverse_section(start,end):
        while start<end:
            chars[start],chars[end]=chars[end],chars[start]
            start,end=start+1,end-1
    reverse_section(0,len(chars)-1)

    start=0
    for end in range(len(chars)):
        if chars[end]==" ":
            reverse_section(start,end-1)
            start=end+1
    reverse_section(start,len(chars)-1)
    return " ".join(("".join(chars)).split())

s = "a good   example"
print(reversed_words_in_place(s))

#4.Zigzag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"






# 5.Find the  Index of the First Occurence in a string
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.