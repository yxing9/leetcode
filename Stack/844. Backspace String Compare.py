# 844. Backspace String Compare
# Easy


# Larry, https://www.youtube.com/watch?v=I5kBbAtUOuw
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def parse(s):
            stack = []
            
            for c in s:
                if c == "#":
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(c)
                    
            return "".join(stack)
        
        return parse(s) == parse(t)
# linear time and space
# 05/03/2022 21:04

# my solution using stack
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []
        
        for _ in s:
            if _ == "#" and len(stack_s) == 0:
                continue
            elif _ == "#" and len(stack_s) != 0:
                stack_s.pop()
            else:
                stack_s.append(_)
                
        for _ in t:
            if _ == "#" and len(stack_t) == 0:
                continue
            elif _ == "#" and len(stack_t) != 0:
                stack_t.pop()
            else:
                stack_t.append(_)
                
        return stack_s == stack_t
# 05/01/2022 18:23
# O(N) or O(M) time whichever is greater, N == s.length, M == t.length
# O(N) or O(M) space whichever is greater, N == s.length, M == t.length