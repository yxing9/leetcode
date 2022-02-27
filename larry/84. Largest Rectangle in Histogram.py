# 84. Largest Rectangle in Histogram
# Hard


"""

Looks like a dp problem.

How to determine it's a rectangle?




"""


# Larry, https://www.youtube.com/watch?v=Nd6lh_yo9ts
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0
        
        for i, h in enumerate(heights):
            leftMost = i
            # how far can we go left before we see a shorter bar
            while len(stack) > 0:
                leftIndex, leftHeight = stack[-1]
                if leftHeight > h:
                    best = max(best, (i - leftIndex) * leftHeight)
                    leftMost = leftIndex
                    stack.pop()
                else:
                    break
                    
            stack.append((leftMost, h))
            
        right = len(heights)
        while len(stack) > 0:
            leftIndex, leftHeight = stack[-1]
            best = max(best, (right - leftIndex) * leftHeight)
            stack.pop()
            
        return best
# 01/29/2022 17:56





# --- END --- #