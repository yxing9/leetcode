# 1029. Two City Scheduling
# Medium


# Larry, https://www.youtube.com/watch?v=M7fSu8bomUw
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        costs.sort(key=lambda c: c[0] - c[1])
        
        total = 0
        for i in range(N):
            if i + i < N:
                total += costs[i][0]
            else:
                total += costs[i][1]
        return total
# 03/25/2022 16:57