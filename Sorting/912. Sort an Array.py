# 912. Sort an Array
# Medium


'''

I think this is the question to practice all sorting algorithms.

1. merge sort

2. quick sort

3. heap sort


'''

# Merge sort solution on geeksforgeeks
# https://www.geeksforgeeks.org/merge-sort/
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        merge sort
        """
        if len(nums) > 1:
            mid = len(nums) // 2
        
            L = nums[:mid]
            R = nums[mid:]
            
            self.sortArray(L)
            self.sortArray(R)
        
            i, j, k = 0, 0, 0
            
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
        
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1
                
            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
        
        return nums
# Runtime: 892 ms, faster than 27.39%
# Memory Usage: 21.5 MB, less than 75.95%
# Compared it against the merge sort solution on 
# https://leetcode.com/problems/sort-an-array/discuss/276916/Python-bubble-insertion-selection-quick-merge-heap
# they are identical. 



# --- End --- #