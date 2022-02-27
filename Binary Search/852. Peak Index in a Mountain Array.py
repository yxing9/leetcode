# 852. Peak Index in a Mountain Array
# Easy
# binary search


'''
Different from #941, 
the array arr is guaranteed to be a mountain array.
We just need to find its peak.
Sounds easier immediately.

[0,1,0]
 l m r

[0,10,5,2]
 0 1  2 3
 l m    r

[3,4,5,1]
 0 1 2 3
 l m   r

[24,69,100,99,79,78,67,36,26,19]
 0  1  2   3  4  5  6  7  8  9
 l            m              r

We can creat a target, max(arr)
but max() is O(n) time with n being arr.length
then binary search is O(logn) time
so combined is O(n) time
what's the point of using binary search?


11/30/2021
given again at pair programming



r = m - 1 must be paired with l <= r
r = m must be paired with l < r


variations can be made upon changing b/t:
return l
or 
return r

arr[m] < arr[m+1]
or 
arr[m] > arr[m+1]

'''


# standard solution
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            m = l + (r - l) // 2
            if arr[m] < arr[m+1]:
                l = m + 1
            else:
                r = m
        return l
# time O(log n)
# space O(1)



# binary search, 11/30/2021
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) # or l, r = 0, len(arr)-1 but I think len(arr) without 1 is a bug
        while l < r: # or while l <= r:
            m = l + (r-l)//2
            if arr[m] < arr[m+1]:
                l = m + 1
            else:
                r = m # or r = m - 1
        return l
# Runtime: 76 ms, faster than 66.90%

# I can also modify to return r
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        while l < r:
            m = l + (r - l) // 2
            if arr[m] > arr[m+1]:
                r = m
            else:
                l = m + 1
        return r
# Runtime: 76 ms, faster than 66.90%

# -----------------------------------------

# binary search, 05/17/2021
class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
        return l
# 51.47%
'''
This is from leetcode solution
based on linear scan of "if arr[i] > arr[i + 1]: return i"
'''

s = Solution()
print(s.peakIndexInMountainArray([0,1,0])) # expect 1
print(s.peakIndexInMountainArray([0,2,1,0])) # expect 1
print(s.peakIndexInMountainArray([0,10,5,2])) # expect 1
print(s.peakIndexInMountainArray([3,4,5,1])) # expect 2
print(s.peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19])) # expect 2