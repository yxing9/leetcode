# 1064. Fixed Point
# Easy
# Locked

'''
3rd question in Binary Search Workshop assignment.

Given an array of distinct integers arr, 
where arr is sorted in ascending order, 
return the smallest index i that satisfies arr[i] == i. 
If there is no such index, return -1.

Example 1:
Input: arr = [-10,-5,0,3,7]
Output: 3
Explanation: For the given array, 
arr[0] = -10, arr[1] = -5, arr[2] = 0, arr[3] = 3, thus the output is 3.

Example 2:
Input: arr = [0,2,5,8,17]
Output: 0
Explanation: arr[0] = 0, thus the output is 0.

Example 3:
Input: arr = [-10,-5,3,4,7,9]
Output: -1
Explanation: There is no such i that arr[i] == i, thus the output is -1.


Constraints:
1 <= arr.length < 104
-109 <= arr[i] <= 109

Follow up: The O(n) solution is very straightforward. Can we do better?
'''

# Thoughts before coding
'''
[-10,-5,0,3,7] 3
 0   1  2 3 4  return index
 l      m   r
          l r
          m


[0,2,5,8,17]
 0 1 2 3 4


[-10,-5,3,4,7,9]
 0   1  2 3 4 5

We just need to know the movement of left and right.
left and righ still represent indices.

We do not need to consider negative elements since indices are >= 0.

Consider the edge case where there is no i matching arr[i].


N.B.: "return the smallest index i that satisfies arr[i] == i"
edge case: [-10,-5,-2,0,4,5,6,7,8,9,10]
'''

class Solution:
    def fixedPoint(self, arr) -> int:
        l, r = 0, len(arr) - 1
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == mid:
                res = mid
                r -= 1
            elif arr[mid] < mid:
                l = mid + 1
            else:
                r = mid - 1
        return res
# 48.00%

# Pathrise solution
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if arr[mid] < mid:
                l = mid + 1
            else:
                r = mid

        if arr[l] == l: return l
        if arr[r] == r: return r
        return -1
# 72.58%

s = Solution()
print(s.fixedPoint([-10,-5,0,3,7])) # expect 3
print(s.fixedPoint([0,2,5,8,17])) # expect 0
print(s.fixedPoint([-10,-5,3,4,7,9])) # expect -1
print(s.fixedPoint([-10,-5,-2,0,4,5,6,7,8,9,10])) # expect 4
print(s.fixedPoint([0,1,2])) # expect 0