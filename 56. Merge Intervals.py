# 56. Merge Intervals
# Medium
# sorting



from typing import List
# neetcode solution 12/07/2021
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        1. sort by starting value since order is not guaranteed
        2. create and preset a res list, which each element of intervals is compared against
        3. update the ending boundary element in res, or add new interval to res
           (don't worry about starting boundaries since the input array is already sorted)
        
        Time: O(n log n)
        Space: O(n)
        n == intervals.length
        '''
        intervals.sort(key=lambda i:i[0])
        res = [intervals[0]]
        for start, end in intervals: # or intervals[1:]
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res
# Runtime: 88 ms, faster than 58.23%



# lc sorting solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
# Runtime: 84 ms, faster than 76.98%
# time O(n log n)
# space O(n)
# space O(log n) if in-place, O(log n) is for sorting



#-------------------------
# my wrong solution 12/07/2021
# solve-able only when intervals.length is even
class SolutionF:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        
        1. ---- a
              ---- b
              
        2.    ---- a
           ---- b
           
        3. ------ a
            --- b
            
        4.  --- a
           ------ b
        
        '''
        if len(intervals) == 1:
            return intervals
        l, r = 0, 1
        res = []
        while l < r and r < len(intervals):
            if intervals[l][0] <= intervals[r][0] and intervals[l][1] >= intervals[r][0] and intervals[r][1] >= intervals[l][1]: # 1.
                res.append([intervals[l][0], intervals[r][1]])
            elif intervals[r][0] <= intervals[l][0] and intervals[r][1] >= intervals[l][0] and intervals[l][1] >= intervals[r][1]: # 2.
                res.append([intervals[r][0], intervals[l][1]])
            elif intervals[l][0] <= intervals[r][0] and intervals[l][1] >= intervals[r][1]: # 3.
                res.append([intervals[l][0], intervals[l][1]])
            elif intervals[r][0] <= intervals[l][0] and intervals[r][1] >= intervals[l][1]: # 4.
                res.append([intervals[r][0], intervals[r][1]])
            else:
                res.append(intervals[l])
                res.append(intervals[r])
            l += 2
            r += 2
        return res

'''
[[1,3],[2,6],[8,10],[15,18]]
[[1,3]]
[[1,4],[0,4]]
[[1,4],[0,1]]
[[1,4],[2,3]]
[[1,4],[0,2],[3,5]]
'''
test0 = [[1,3],[2,6],[8,10],[15,18]] # expect [[1,6],[8,10],[15,18]]
test1 = [[1,3]] # expect [[1,3]]
test2 = [[1,4],[0,4]] # expect [[0,4]]
test3 = [[1,4],[0,1]] # expect [[0,4]]
test4 = [[1,4],[2,3]] # expect [[1,4]]
test5 = [[1,4],[0,2],[3,5]] # expect [[0,5]]

s = SolutionF()
print(s.merge(test0))
print(s.merge(test1))
print(s.merge(test2))
print(s.merge(test3))
print(s.merge(test4))
print(s.merge(test5)) # failed