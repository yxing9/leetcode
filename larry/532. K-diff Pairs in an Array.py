# 532. K-diff Pairs in an Array
# Medium



"""

unique pairs
    res int []
    check if new_pair in res

"""

# larry, https://www.youtube.com/watch?v=Ce6R9HcCvdU
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        lookup = set()
        seen = set()

        for x in nums:
            # |x - p| = k
            # x - p  = k
            # x - k  = p
            #
            # x - p = -k
            # x + k = p

            if x - k in lookup:
                seen.add(x - k)

            if x + k in lookup:
                seen.add(x)

            lookup.add(x)

        return len(seen)
