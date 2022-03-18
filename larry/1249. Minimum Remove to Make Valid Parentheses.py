# 1249. Minimum Remove to Make Valid Parentheses
# Medium


# Larry, https://www.youtube.com/watch?v=cN2rZeWwmwI
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack will contain the indices of the open parens
        stack = []
        N = len(s)
        deleted = [False] * N
        
        for i, c in enumerate(s):
            if c in "()":
                if c == "(":
                    stack.append(i)    
                else:
                    if len(stack) == 0:
                        deleted[i] = True
                    else:
                        stack.pop()    
            else:
                # alphabet
                continue
                
        for i in stack:
            deleted[i] = True
            
        ans = []
        for i in range(N):
            if not deleted[i]:
                ans.append(s[i])
        return "".join(ans)
# 03/15/2022 17:04