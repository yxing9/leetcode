# 88. Merge Sorted Array
# Easy

# Introduction to Data Structure
# Arrays 101

# Related Topics
# Array
# Two Pointers

# Similar Questons
'''
Merge Two Sorted Lists
Easy
Squares of a Sorted Array
Easy
Interval List Intersections
Medium
'''



# Two Pointers: in-place 08/02/2021
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = m-1, n-1
        curr = len(nums1)-1
        while l >= 0 and r >= 0:
            if nums1[l] < nums2[r]:
                nums1[curr] = nums2[r]
                r -= 1
            else:
                nums1[curr] = nums1[l]
                l -= 1
            curr -= 1
        while r >= 0:
            nums1[curr] = nums2[r]
            r -= 1
            curr -= 1
# time: O(n)
# space: O(1)
# Two Pointers: out of place 08/02/2021
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        '''
        This is an out-of-place solution.
        '''
        res = []
        l, r = 0, 0
        while l < m and r < n:
            if nums1[l] < nums2[r]:
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r += 1
        while l < m:
            res.append(nums1[l])
            l += 1
        while r < n:
            res.append(nums2[r])
            r += 1
        return res
s = Solution()
print(s.merge([1,3,4,7,12], 5, [3,6,6], 3)) # expect [1,3,3,4,6,6,7,12]




# Brute force
# I. First compare then add to nums1
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        1,2,3,0,0,0
          2,  5,6

        """
        for n1 in nums1:
            for n2 in nums2:
                if n2 > n1:
                    nums1.insert(nums1.index(n1), n2)
                    nums1.pop()

        print(n1)
# i think this is incomplete


# II. 04/25/2021
# Migrate all elements of nums2 to nums1 then sort nums1 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for n2 in nums2:
            nums1[m] = n2
            m += 1
        
        nums1.sort()
        
        return nums1
# 88.06 % 
# time: O(n log n) sorting 
# This is a very easy solution I wrote very quickly


# III. 10/13/2020
# Here a solution I? submitted on 10/13/2020 14:32
# Today's date is 4/25/2021
# But I don't remember writing this solution
# Along with it are 2 wrong submissions with the same two-pointers approach
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Make initialized position of the two pointers and new merged list
        index1 = m - 1
        index2 = n - 1
        indexMerged = m + n - 1
        
        # Migrate numbers from nums2 to nums1 
        # Use indexMerged for the update of the final result list 
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] <= nums2[index2]:
                nums1[indexMerged] = nums2[index2]
                index2 -= 1
            else:
                nums1[indexMerged] = nums1[index1]
                index1 -= 1
            indexMerged -= 1
            
        # If there is any number left uncompared in either list, put it to the result list
        while index1 >= 0:
            nums1[indexMerged] = nums1[index1]
            indexMerged -= 1
            index1 -= 1
        
        while index2 >= 0:
            nums1[indexMerged] = nums2[index2]
            indexMerged -= 1
            index2 -= 1
# 67.14 %



# Test Cases
s = Solution()
print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(s.merge([1],1,[],0))