# 1636. Sort Array by Increasing Frequency
# Easy
# https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums):
        '''
        This is Tim Nguyen's solution.
        '''
        
        repeats = dict()
        ret = []

        for num in nums:
            if num not in repeats:
                repeats[num] = 1
            else:
                repeats[num] += 1  
        
        repeats = sorted(repeats.items(), key=lambda x: x[0], reverse=True)
        repeats = sorted(repeats, key=lambda x: x[1])
        
        for x, y in repeats:
            for i in range(y):
                ret.append(x)
                
        return ret
# 77.77%

from heapq import *
from collections import defaultdict
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Neena Shereen

# store num and fre d = {num:freq}

num=key and feq is value

nums = [2,3,1,3,2]

dic= {2:2,3:2,1:1}


minheap={(freq,-val)} (1,-1) (2,-3),(2,-2)

 pop out = (1,1) ans= [1]
 
 pop out = (2,3)
        
        """
        # dictionary
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        # heapify
        temp=[(freq,-val) for val,freq in d.items()]
        heap = []
        for i in temp:
            heappush(heap,i)
        ans=[]
        while heap: 
            f,v= heappop(heap)
            temp=[-v]*f
            ans+=temp
        
        return ans


# Test Cases
s = Solution()
print(s.frequencySort([1,1,2,2,2,3])) #-> [3,1,1,2,2,2]
print(s.frequencySort([2,3,1,3,2])) #-> [1,3,3,2,2]
print(s.frequencySort([-1,1,-6,4,5,-6,1,4,1])) #-> [5,-1,4,4,-6,-6,1,1,1]
