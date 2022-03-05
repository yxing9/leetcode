# 740. Delete and Earn
# Medium



# Larry, https://www.youtube.com/watch?v=RL2dzvSUVSg
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        # O(N log N)
        uniq = list(sorted(list(set(nums))))

        N = len(uniq)

        cache = [None] * N
        has_cache = [False] * N

        # index -> 0 to N -> O(N) number of input
        # each index is O(1) space -> O(N) space
        # each index is O(1) time -> O(N) time
        def go(index):
            if index >= N:
                return 0

            if has_cache[index]:
                return cache[index]

            current = uniq[index] * counter[uniq[index]]

            if index + 1 < N and uniq[index] + 1 == uniq[index + 1]:
                take = current + go(index + 2)
            else:
                take = current + go(index + 1)
            
            skip = go(index + 1)

            has_cache[index] = True
            cache[index] = max(take, skip)
            return cache[index]

        return go(0)
# 03/05/2022 17:35