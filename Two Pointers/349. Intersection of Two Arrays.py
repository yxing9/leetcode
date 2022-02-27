# 349. Intersection of Two Arrays
# Easy


# Two Pointers
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        l, r = 0, 0
        res = []
        while l < len(nums1) and r < len(nums2):
            if nums1[l] != nums2[r]:
                if nums1[l] < nums2[r]:
                    l += 1
                else:
                    r += 1
            else:
                if nums1[l] not in res:
                    res.append(nums1[l])
                l += 1
                r += 1
        return res
# time: O(n log n + m log m) with n being len(nums1) and m being len(nums2)
# space: O(n + m)
# to refactor the code
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                l += 1
            elif nums1[l] > nums2[r]:
                r += 1
            else:
                if nums1[l] not in res:
                    res.append(nums1[l])
                l += 1
                r += 1
