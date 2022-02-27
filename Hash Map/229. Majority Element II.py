# 229. Majority Element II
# Medium

# hash map
# Boyer-Moore Majority Vote Algorithm

# Similar questions: 
# 169.


# hash map
# my solution
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        
        find all
        
        I can still use hash map with O(n) time and O(n) space.
        But the question wants linear time and O(1) space.
        
        What about sorting?
        
        '''
        
        n = len(nums)
        hashmap = {}
        res = []
        
        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
            hashmap[nums[i]] += 1
        for k,v in hashmap.items():
            if v > n / 3:
                res.append(k)
        
        return res
# Runtime: 120 ms, faster than 58.49%
# time O(n)
# space O(n)
# This is an easy medium question if through this solution, 
# the same as 169.


# use 