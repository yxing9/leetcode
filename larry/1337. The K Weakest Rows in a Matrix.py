# 1337. The K Weakest Rows in a Matrix
# Easy


# Larry, https://www.youtube.com/watch?v=O5ORwC3wsVw
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # R = rows
        # C = columns
        h = []
        
        # O(R * C * log k + k) time
        # O(R) space
        for index, row in enumerate(mat):
            heapq.heappush(h, (-row.count(1), -index))
                           
            while len(h) > k:
                heapq.heappop(h)
                       
        ans = []
        while len(h) > 0:
            _, index = heapq.heappop(h)
            index = -index

            ans.append (index)
                       
        ans.reverse()
        return ans
# 03/27/2022 19:43