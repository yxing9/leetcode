# 525. Contiguous Array
# Medium


# Larry's, https://www.youtube.com/watch?v=zI33K2Ck7n8
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {}
        
        seen[0] = -1
        best = 0
        # current will keep track of the number of 1's minus number of 0's
        current = 0
        for index, x in enumerate(nums):
            if x == 1:
                current += 1
            else:
                current -= 1

            # have we seen this before?
            if current in seen:
                best = max(best, index - seen[current])
            else:
                seen[current] = index
        return best
# 02/04/2022 16:02




# --- END --- #