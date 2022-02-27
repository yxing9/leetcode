# Longest Valid Parentheses
# Leetcode 32
# Hard

# Given a string containing just the characters '(' and ')', 
# find the length of the longest valid (well-formed) parentheses substring.
'''
Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0 

Input:  ()(()))))
Output: 6
Explanation:  ()(())

()
2
'''

# Stack with -1
# It is genius to use -1 as the first item in the stack,
# so that "()" can be correctly caculated as 2. 
def longestValidParentheses(s):
    n = len(s)
    stack = [-1]
    result = 0

    for i in range(n):
        if s[i] == "(":
            stack.append(i)
        
        else:
            stack.pop()
            if len(stack) != 0:
                result = max(result, i - stack[-1])
            else:
                stack.append(i)
    
    return result

# Tests
s1 = "()"
print(longestValidParentheses(s1))
# 2

s2 = "(()"
print(longestValidParentheses(s2))
# 2

s3 = "()(()))))"
print(longestValidParentheses(s3))
# 6

s4 = ""
print(longestValidParentheses(s4))
# 0

s5 = "((()()"
print(longestValidParentheses(s5))
# 4

s6 = "()(()))))()()()()"
print(longestValidParentheses(s6))
# 8