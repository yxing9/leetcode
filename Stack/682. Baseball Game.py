# 682. Baseball Game
# Easy


# my stack solution
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for i in ops:
            if i.lstrip("-").isdigit():
                stack.append(int(i))
                
            elif i == "+":
                stack.append(stack[-2] + stack[-1])
            
            elif i == "D":
                stack.append(stack[-1] * 2)
            
            elif i == "C":
                stack.pop()
        
        return sum(stack)
# 04/10/2022 16:03
# O(N) time
# O(N) space
# N.B. the negative numbers


# Larry, https://www.youtube.com/watch?v=vs2SmUzBGfc
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for op in ops:
            if op == "+":
                x, y = stack[-1], stack[-2]
                stack.append(x + y)
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
# 04/10/2022 18:50