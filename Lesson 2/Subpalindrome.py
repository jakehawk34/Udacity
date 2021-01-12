# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice_matrix(s):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    if len(s) == 0:
        return 0, 0
    s = s.lower()
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
    max_length = 1
    start = 0
    for l in range(2,len(s)+1):
        for i in range(len(s)-l+1):
            end = i+l
            if l==2:
               if s[i] == s[end-1]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
                  #print('Current longest substring here: {}, {}'.format(start, start + max_length))
                  #print(dp)
            else:
               if s[i] == s[end-1] and dp[i+1][end-2]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
                  #print('Current longest substring there: {}, {}'.format(start, start + max_length))
                  #print(dp)
    return start, start + max_length

matrix = longest_subpalindrome_slice_matrix

'''print(matrix('level'))
print(matrix('Racecar'))
print(matrix('RacecarX'))
print(matrix(''))
print(matrix('something rac e car going'))'''

def longest_subpalindrome_slice_center(string):
    string = string.lower()
    if len(string) == 0:
        return (0, 0)
    maxLength = 1
  
    start = 0
    length = len(string) 
  
    low = 0
    high = 0
  
    # One by one consider every character as center point of  
    # even and length palindromes 
    for i in range(1, length): 
        # Find the longest even length palindrome with center 
    # points as i-1 and i. 
        low = i - 1
        high = i 
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
  
        # Find the longest odd length palindrome with center  
        # point as i 
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
  
    print("Longest palindrome substring is:"), 
    print(string[start:start + maxLength])
  
    return start, start + maxLength

center = longest_subpalindrome_slice_center

print(center('RacecarXhHannahH'))
print(center(''))
print(center('something rac e car going'))

    
def test():
    L = longest_subpalindrome_slice_center
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print(test())

