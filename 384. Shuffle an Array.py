# 384. Shuffle an Array
# Medium


'''

To reset, just return the original input of the array
To shuffle, use random.shuffle()


I don't know which data structure and/or algorithms to use.


The main idea would be:
use random.shuffle to shuffle()
make a copy of the original array and use the copy to revert to the original array

But it is missing the point.
'''


'''
https://leetcode.com/problems/shuffle-an-array/discuss/85957/easy-python-solution-based-on-generating-random-index-and-swapping
'''


# The most straightforward
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        ans = self.nums[:]
        for i in range(len(ans)):
            j = random.randrange(0, i+1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans

# ----

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        ans = self.original[:] # or ans = list(self.original)
        for i in range(len(ans)):
            j = random.randrange(0, i+1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


# ----

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# ----

class Solution:
    def __init__(self, nums):
        self.nums = nums[:]
    def reset(self):
        return self.nums
    def shuffle(self):
        ans = self.nums[:]
        random.shuffle(ans)
        return ans