# 287. Find the Duplicate Number
# Medium


# Larry, https://www.youtube.com/watch?v=RTXKETrznc8
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # binary search ->
        # count how many numbers there are that is "x" or larger
        # take the half that has >= half the numbers
        # O(N log N) time
        # log N iterations, O(N) each
        # O(1) space
        
        # swap cycle solution ->
        # O(N) time, O(1) extra space
        # "swaps" nums[i] with the nums[nums[i]] until we see a repeat
        # but, modifies nums in place
        
        # building off the swap cycle solution but without the swapping
        # Floyd's cycle detection -> tortoise and the hare
        # (think of the linked list solution)
        
        N = len(nums)
        slow = N - 1
        fast = N - 1
        
        # [2,1,1,1,4]
        #
        # 4, 4
        # 1, 2
        # 2, 2
        first = True
        while first or slow != fast:
            slow = nums[slow] - 1
            fast = nums[fast] - 1
            fast = nums[fast] - 1
            first = False
            
        fast = N - 1
        while slow != fast:
            slow = nums[slow] - 1
            fast = nums[fast] - 1
            
        # Find cycle in a linked list
        return slow + 1
# 03/29/2022 17:42