# 80. Remove Duplicates from Sorted Array II
# Medium



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Larry, https://www.youtube.com/watch?v=t-_CSLAO1ho
        """
        N = len(nums)

        left = 1
        for right in range(1, N):
            nums[left] = nums[right]
            left += 1

            if left >= 3 and nums[left - 1] == nums[left - 2] and nums[left - 1] == nums[left - 3]:
                left -= 1

        return left
# 02/13/2022 20:20