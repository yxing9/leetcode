# 20. Valid Parentheses
# Easy
# https://leetcode.com/problems/valid-parentheses/
# string, stack


# Larry, https://www.youtube.com/watch?v=X9jT1zDeS3I
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        for p in s:
            if p in "([{":
                stack.append(p)
                continue
            else:
                if len(stack) == 0 or stack[-1] != matching[p]:
                    return False
                stack.pop()
                
        return len(stack) == 0
# 03/13/2022 18:59

# --------------------------

# August 7, 2021
'''

stack:
1. when do we want to add to stack: 
    1. when it is empty
    or
    2. when we have an opening bracket
2. when do we want to pop from stack:
    1. only when a closing bracket has a match


'''
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in s:
            if not stack or i not in mapping: # if stack is empty or i is an opening bracket
                stack.append(i)
            if i in mapping: # meaning i is a closing bracket
                if mapping[i] == stack[-1]: # i is a closing bracket, mapping[i] is the right of the colon
                    stack.pop()
                elif mapping[i] != stack[-1]: # or if this is the first time we enter that closing bracket
                    stack.append(i)
        return not stack


s = Solution()
print(s.isValid("()")) # expect True
print(s.isValid("()[]{}")) # expect True
print(s.isValid("(]")) # expect False
print(s.isValid("([)]")) # expect False
print(s.isValid("{[]}")) # expect True
print(s.isValid("(])")) # expect False

'''

In this question, I find leetcode solution can be hard to understand 
maybe because of the way it explains or the way its code is written.

'''