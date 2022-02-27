# 169. Majority Element
# Easy

# hash map
# sorting and math
# randomization
# divide and conquer
# Boyer-Moore Voting Algorithm

'''

similar to 1150 but not using binary search 
since the array is not sorted

solution 1: using hash map
need to do better than O(n) space

solution 2: sorting and math
used the assumption that the majority element always exists


many more good solutions on https://leetcode.com/problems/majority-element/solution/

'''


# hash map
# my solution 12/01
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
        if max(hashmap.values()) > n / 2:
            return max(hashmap, key=hashmap.get)
# Runtime: 176 ms, faster than 45.80%
# time O(n)
# space O(n)



# solution 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
# Runtime: 160 ms, faster than 89.04%
# time O(n log n)
# space O(1) (O(n) if in-place sorting is not allowed)
# i don't understand this solution.