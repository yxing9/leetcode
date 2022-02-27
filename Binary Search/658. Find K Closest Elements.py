# 658. Find K Closest Elements
# Medium
# https://leetcode.com/problems/find-k-closest-elements/

'''
[1,2,3,4,5] x = 3
 i i x i

-1, [1,2,3,4,5] x = -1
     i i i i


N.B.
1. Elements are not distince.t
We can't use abs(x - arr[l/r]) because the question does not state 
 elements in the array are distinct.

2. x might not be in the array.


In the end, what we return is arr[i]:arr[i + k] not inclusive of arr[i + k]
We compare distance from x to the two ends of our range: 
arr[i] and arr[i + k]
and we get 
x - arr[i] and arr[i + k] - x

It can be:
    arr[i]       x    arr[i + k]   

or:
    arr[i]     arr[i + k]     x    

or:
    x     arr[i]     arr[i + k]    

'''

class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        l, r = 0, len(arr) - k

        while l < r:
            mid = l + (r - l) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid

        return arr[l:l+k]
# Time O(log(n-k)) n is arr.length
# 90.76%
'''
Why "r = mid" not "r = mid - 1"?
Because leftward is inclusive but rightward is not inclusive.
'''

s = Solution()
print(s.findClosestElements([1,2,3,4,5], 4, 3)) # expect [1,2,3,4]
print(s.findClosestElements([1,2,3,4,5], 4, -1)) # expect [1,2,3,4]
print(s.findClosestElements([1,2,3,4,5], 4, 6)) # expect [2,3,4,5]
print(s.findClosestElements([0,2,2,3,4,6,7,8,9,9], 4, 5)) # expect [3,4,6,7]