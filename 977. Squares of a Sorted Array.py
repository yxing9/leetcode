# 977. Squares of a Sorted Array
# Easy
# 3rd problem in Leetcode's Array Introduction chapter
# Seemingly easy but have great depth to dive into

'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''
# Thoughts
# Wording of the problem description is confusing. 
#   Why saying "non-decreasing" order instead of increasing order. 

# Brute force
# First square all
# Then sort squared
# Done
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        unsorted_square = []
        
        for num in nums:
            unsorted_square.append(num ** 2)
        
        unsorted_square.sort()
        
        return unsorted_square
# 54.76 %
# Squaring each num is O(n)
# Pyton list.sort() is Timsort and is O(nlogn)
# O(n + n * log n) in total
# O(n) needed

# Other Great Solutions:
# https://leetcode.com/problems/squares-of-a-sorted-array/discuss/1160450/Python-Stack-O(n)-memory-O(n)
# https://leetcode.com/problems/squares-of-a-sorted-array/discuss/310865/Python%3A-A-comparison-of-lots-of-approaches!-Sorting-two-pointers-deque-iterator-generator
'''
Something slightly irritating is that leetcode isn't testing with big enough test cases 
to push the time complexity of the O(n-log-n) approaches below the O(n) ones. 
It goes to show, sometimes what "wins" at the notoriously inaccurate Leetcode time/ space percentiles 
isn't always the best in practice, or even in an interview.

I think it's best to ask your interviewer if they want something done in-place or not. 
It is a common misconception that we should always be trying to do things in-place, overwriting the inputs.
'''