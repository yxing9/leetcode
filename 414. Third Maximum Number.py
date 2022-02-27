# 414. Third Maximum Number
# Easy


# Brute force using sorted()
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]
# time: O(n log n) for tim sort
# space: O(1) modified in-place


# Heap
