# 946. Validate Stack Sequences
# Medium



# Larry, https://www.youtube.com/watch?v=81WO_JtWpk8
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N = len(pushed)
        
        stack = []
        index = 0
        
        for item in pushed:
            stack.append(item)
            
            while len(stack) > 0 and index < N and popped[index] == stack[-1]:
                stack.pop()
                index += 1
                
        return index == N
# 03/16/2022 15:16