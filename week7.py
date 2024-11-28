#1.Text Justification
# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.
# Example 3:

# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

def text_just(words,maxWidth):
    current_line=[]
    result=[]
    current_length=0
    for word in words:
        if current_length+len(word)+len(current_line)>maxWidth:
            for i in range(maxWidth-current_length):
                current_line[i%(len(current_line)-1 or 1)]+=" "
            result.append("".join(current_line))
            current_line,current_length=[],0
        current_line.append(word)
        current_length+=len(word)
    result.append("".join(current_line).ljust(maxWidth))
    return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth=16
print("\n".join(text_just(words,maxWidth)))   

def justification(words,maxWidth):
    result=[]
    line=[]
    line_length=0
    for word in words:
        if line_length + len(line) + len(word) > maxWidth:
            result.append(line)
            line = []
            line_length = 0
        line.append(word)
        line_length += len(word)
    result.append(line)
    justified_result = []
    for i in range(len(result)):
        line = result[i]
        if i == len(result) - 1 or len(line) == 1:
            justified_result.append(" ".join(line).ljust(maxWidth))
        else:
            spaces = maxWidth - sum(len(word) for word in line)
            gaps = len(line) - 1

            if gaps > 0:
                space_per_gap = spaces // gaps
                extra_spaces = spaces % gaps
                justified_line = ""
                for j in range(gaps):
                    justified_line += line[j] + " " * (space_per_gap + (1 if j < extra_spaces else 0))
                justified_line += line[-1]
                justified_result.append(justified_line)
            else:
                 justified_result.append(line[0].ljust(maxWidth))
    return justified_result

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth=16
print("\n".join(justification(words,maxWidth)))



#2.  Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


#3.Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Substring any portion of the string which is consecutive in nature 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def subString(s):
    maxLength=0
    visited=[False]*256
    left=0
    right=0
    while right<len(s):
        while visited[ord(s[right])]==True:





#4. Substring with Concatenation of All Words

# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 
# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Explanation:

# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []

# Explanation:

# There is no concatenated substring.

# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

# Output: [6,9,12]

# Explanation:

# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

# 5.Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 