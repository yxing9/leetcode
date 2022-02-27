# 1675. Minimize Deviation in Array
# Hard


# larry, https://www.youtube.com/watch?v=lKzGBqxNyLM
from sortedcontainers import SortedList

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        sl = SortedList(nums)
        best = sl[-1] - sl[0]

        # N = len(nums)
        # R = 10^9

        # O(N log N log R) time
        # O(N) space
        while sl[0] % 2 == 1:
            v = sl[0]
            sl.remove(v)
            sl.add(v * 2)
            best = min(best, sl[-1] - sl[0])

        while sl[-1] % 2 == 0:
            v = sl[-1]
            sl.remove(v)
            sl.add(v // 2)
            best = min(best, sl[-1] - sl[0])

        while sl[0] % 2 == 1:
            v = sl[0]
            sl.remove(v)
            sl.add(v * 2)
            best = min(best, sl[-1] - sl[0])

        return best
# 02/19/2022 16:04