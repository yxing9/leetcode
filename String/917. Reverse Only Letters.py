# 917. Reverse Only Letters
# Easy


# my solution
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = 'abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        l, r = 0, len(s)-1
        lst = list(s)
        while l < r:
            if lst[l] not in letters:
                l += 1
            if lst[r] not in letters:
                r -= 1
            if lst[l] in letters and lst[r] in letters:
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1
        s = ''.join(lst)
        return s
# Runtime: 28 ms, faster than 92.99%
# time: O(n)



# pathrise solution (pair programming)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        def isAlpha(letter):
            letters = 'abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if letter in letters:
                return True
            return False
        
        ans = []
        j = len(s) - 1
        for i,x in enumerate(s):
            if isAlpha(x):
                while not isAlpha(s[j]):
                    j -= 1
                ans.append(s[j])
                j -= 1
            else:
                ans.append(x)
        
        return "".join(ans)
# Runtime: 32 ms, faster than 82.02%
# time: O(n)

'''

edge cases:

input
expected

"z<*zj"
"j<*zz"

"7_28]"
"7_28]"


'''