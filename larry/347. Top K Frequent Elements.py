# 347. Top K Frequent Elements
# Medium


# Larry, https://www.youtube.com/watch?v=X6XAK-ZeOgQ
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(N) time
        # O(N) space
        count = collections.Counter(nums)

        h = []
        # O(N) iterations
        for key, c in count.items():
            # O(log K)
            heapq.heappush(h, (c, key))

            if len(h) > k:
                heapq.heappop(h)

        # O(N log K) time
        # O(N + K) space
        return list(key for c, key in h)
# 04/11/2022 21:54