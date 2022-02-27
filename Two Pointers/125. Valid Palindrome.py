# 125. Valid Palindrome
# Easy
# https://leetcode.com/problems/valid-palindrome/


# Two Pointers
# use .isalnum() in python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
# time: O(n)
# space: O(1) it doesn't take extra space
'''

Note:

elif cannot be written as if
because you only want to do one condition in one loop

s = "A man, a plan, a canal: Panama"
In an edge case of "A man, a
s[l] is moved to become "space" and immediately compared 
to s[r], which is "a"
we get a false result.

'''