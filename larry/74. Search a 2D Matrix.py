# 74. Search a 2D Matrix
# Medium


# Larry, https://www.youtube.com/watch?v=3uy55AvSLNA
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        
        left = 0
        right = R * C - 1
        
        # f maps a 1-D coordinate "t" into x, y
        def f(t):
            x, y = t // C, t % C
            
            return matrix[x][y]
        
        # is the value at position "t" > target
        def good(t):
            return f(t) > target
        
        while left < right:
            mid = (left + right + 1) // 2
            
            if good(mid):
                right = mid - 1
            else:
                left = mid
                
        return f(left) == target
# 03/30/2022 15:10