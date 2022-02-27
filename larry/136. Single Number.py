# 136. Single Number
# Easy
# Bit Manipulation


# My O(N) time and O(N) space solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for k,v in hashmap.items():
            if v == 1:
                return k
# 02/15/2022 00:40



# Larry, XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=woYPvJM9cjM

        O(N) time
        O(1) space
        """
        x = 0
        for y in nums:
            x ^= y
        return x
# 02/15/2022 01:06
# print(0^4^1^2^1^2) -> 4


# --- END --- #