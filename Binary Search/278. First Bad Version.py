# 278. First Bad Version
# Easy


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        l, r = 1, n
        while l < r:
            mid = l + (r-l)//2
            if not isBadVersion(l) and isBadVersion(r) and l + 1 == r:
                return r
            if not isBadVersion(mid):
                l = mid
            if isBadVersion(mid):
                r = mid
# Runtime: 32 ms, faster than 65.70%









class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l + 1 < r:
            mid = l + (r-l)//2
            if not isBadVersion(mid):
                l = mid + 1
            if isBadVersion(mid):
                r = mid - 1
        if not isBadVersion(l) and isBadVersion(r):
            return r