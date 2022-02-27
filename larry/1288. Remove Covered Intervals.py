# 1288. Remove Covered Intervals
# Medium



class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        Larry, https://www.youtube.com/watch?v=ilpLx9-CNKw
        """
        N = len(intervals)
        
        covered = [False] * N
        for i in range(N):
            for j in range(N):
                if i != j:
                    if intervals[i][0] <= intervals[j][0] and intervals[j][1] <= intervals[i][1]:
                        covered[j] = True
                        
        count = 0
        for i in range(N):
            if not covered[i]:
                count += 1
        return count
# 02/20/2022 02:43