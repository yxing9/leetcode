# 921. Minimum Add to Make Parentheses Valid


# My version
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        '''
        def isValid(s):
            pass
            
        if isValid(s):
            return 0
        else:
        '''    
            
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            else:
                if s[i] == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(s[i])
                else:
                    stack.append(s[i])
        return len(stack)
# Runtime: 50 ms, faster than 14.39%
# Time: O(n) 



# leetcode sample 8 ms submission
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        counter = 0
        total = 0
        for i in range(len(s)):
            if s[i] == ')':
                counter -= 1
                if counter < 0:
                    total += 1
                    counter = 0
            else:
                counter += 1
        return counter + total
# Runtime: 32 ms, faster than 71.33%



s = Solution()
print(s.minAddToMakeValid("())")) # expect 1
print(s.minAddToMakeValid("(((")) # expect 3
print(s.minAddToMakeValid("()")) # expect 0
print(s.minAddToMakeValid("()))((")) # expect 4
print('expect 3; actual output is', s.minAddToMakeValid(")))"))