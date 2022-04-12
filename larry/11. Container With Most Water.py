# 11. Container With Most Water
# Medium


# Larry, https://www.youtube.com/watch?v=ytw0lyfuQmI
class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        
        def getMaxArea(height):
            best = 0
            heights = []
            
            for i, right in enumerate(height):
                index = bisect.bisect_left(heights, (right, -1))
                
                if index >= len(heights):
                    heights.append((right, i))
                else:
                    area = right * (i - heights[index][1])
                    best = max(area, best)
            return best
        
        return max(getMaxArea(height), getMaxArea(height[::-1]))
# 04/05/2022 16:22