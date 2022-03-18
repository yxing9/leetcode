# 856. Score of Parentheses
# Medium



# Larry, https://www.youtube.com/watch?v=QM7YYNFcgAU
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for c in s:
            if c == "(":
                stack.append("(")
            else:
                current = 0
                while stack[-1] != "(":
                    current += stack[-1]
                    stack.pop()
                    
                stack.pop()
                if current == 0:
                    stack.append(1)
                else:
                    stack.append(2 * current)
                    
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            
            stack.append(a + b)
        return stack[-1]
# 03/17/2022 15:42