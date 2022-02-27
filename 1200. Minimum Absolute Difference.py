# 1200. Minimum Absolute Difference
# Easy
# 1. sorting with 2 traversals
# 2. sorting with 1 traversal


'''

12/19/2021

Key steps:
1. Get the min absolute by sorting and traversing the sorted array,
    it's O(n log n)
2. Find all pairs of [a,b] to the output arr, a < b
    depending on how you want to find all pairs, can be O(n2)

time O(n log n)
space O(n) <- O(2(n-1))

--------

Where to take advantage:
1. distinct int: can easily be sorted and get max and 2nd max 


Notice:
1. min absolute can be from anywhere, 
    not only max and 2nd max or min and 2nd min as I thought

2. min absolute can only come from two adjacent numbers, 
    it is essentially the distance between them
    so only need to compare adjacent pairs


This is a great edge case [40,11,26,27,-20], 
showing min abs can be from anywhere.




'''

# 1. 
# my original solution - passed
# sorting with 2 traversals
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minAbs = float('inf')
        res = []
        
        i, j = 0, 1
        while j < len(arr):
            minAbs = min(minAbs, abs(arr[i] - arr[j]))
            i += 1
            j += 1
            
        l, r = 0, 1
        while r < len(arr):
            if abs(arr[l] - arr[r]) == minAbs:
                res.append([arr[l], arr[r]])
            l += 1
            r += 1
        
        return res
# Runtime: 396 ms, faster than 32.31%
# time O(n log n) for sorting
# space O(n)
# This is a quite naive solution imo, 
# better do everything in one pass, is it possible? => Yes.


# 1. 
# Nick White's solution (and I wrote it in python)
# still sorting with 2 traversals but without the pointers
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        res = []
        
        for i in range(1, len(arr)):
            min_diff = min(min_diff, abs(arr[i] - arr[i-1]))
            
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) == min_diff:
                res.append([arr[i-1], arr[i]])
                
        return res
# Runtime: 352 ms, faster than 55.70%
# looks better for a 2 traversals solution


# 2. 
# sorting with 1 traversal
# my code and lc solution
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = arr[1] - arr[0]
        res = []
        
        for i in range(1, len(arr)):
            cur_diff = abs(arr[i] - arr[i-1])
            if cur_diff == min_diff:
                res.append([arr[i-1], arr[i]])
            elif cur_diff < min_diff:
                res = [[arr[i-1], arr[i]]]
                min_diff = cur_diff
                
        return res
# Runtime: 328 ms, faster than 85.03%



# --- End --- #