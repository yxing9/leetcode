# 680. Valid Palindrome II
# Easy


# Larry, https://www.youtube.com/watch?v=RoBmHhxCw9U
class Solution:
    def validPalindrome(self, s: str) -> bool:
        N = len(s)
        
        left = 0
        right = N - 1
        
        while left < right:
            if s[left] != s[right]:
                # this is the first and only possible place where is can differ
                if s[left+1:right+1] == s[left+1:right+1][::-1]:
                    return True
                if s[left:right+1-1] == s[left:right+1-1][::-1]:
                    return True
                return False
            left += 1
            right -= 1
        return True
# 04/02/2022 19:55


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                one,two = s[l:r], s[l + 1:r + 1]
                return one == one[::-1] or two == two[::-1]
            l += 1
            r -= 1
        return True
# 10/04/2020 13:51