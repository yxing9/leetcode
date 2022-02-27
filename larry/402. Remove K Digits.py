# 402. Remove K Digits
# Medium


# Larry, https://www.youtube.com/watch?v=5abNoKDhups
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        N = len(num)
        if N == k:
            return "0"

        lookup = collections.defaultdict(collections.deque)
        for index, x in enumerate(num):
            lookup[int(x)].append(index)

        remove = [False] * N

        index = 0
        while index < N:
            current = int(num[index])
        
            for i in range(current):
                while len(lookup[i]) > 0 and lookup[i][0] < index:
                    lookup[i].popleft()

                if len(lookup[i]) > 0 and lookup[i][0] - index <= k:
                    k -= lookup[i][0] - index
                    for x in range(index, lookup[i][0]):
                        remove[x] = True
                    index = lookup[i][0]
                    break
            else:
                index += 1

        ans = "".join(x for r, x in zip(remove, num) if not r).lstrip("0")
        # if there is k leftover, it must be an increasing subsequence
        if k > 0:
            ans = ans[:-k]

        if len(ans) == 0:
            return "0"

        return ans
# 02/18/2022 02:08