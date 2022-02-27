# 344. Reverse String
# Easy
# https://leetcode.com/problems/reverse-string/

#----------

# Two Pointers 08/01/2021
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s
# time: O(n) n is len(s)
# space: O(1) modified in-place

#----------

# Recursion 06/28/2021
'''
To be solved using recursion

But we can test and explore other ways to solve it


Important to know how fibonacci works:

def fib(n):
    if n < 0:
        return
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(9))
print(fib(20))


- How to print a string reversly:
def reverseString(s):
    helper(0, s)
def helper(i, s):
    if i == len(s):
        return
    helper(i+1, s)
    print(s[i])
reverseString("Helloworld")


- How to reverse a string in-place:
def reverseString(s) -> None:
    helper(0, len(s)-1, s)
    return s
def helper(i, j, s):
    if i == j:
        return
    helper(i+1, j-1, s)
    s[i], s[j] = s[j], s[i]
print(reverseString(["h","e","l","l","o"]))
'''

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(i, j, s):
            if i == j or i == len(s)/2:
                return
            helper(i+1, j-1, s)
            s[i], s[j] = s[j], s[i]
        helper(0, len(s)-1, s)
        # return s
# Accepted 220 ms 45.5 MB
# s = Solution()
# print(s.reverseString(["h","e","l","l","o"]))
# print(s.reverseString(["H","a","n","n","a","h"]))



# Other solutions
# class AltenateSolution:
#     def reverseStringIteratively(self, s) -> None:
#         str = []
#         for i in s:
#             str.insert(0, i)
#         return str


#     def reverseStringViaStack(self, s):
#         stack = []
#         str = []
#         for i in range(len(s)):
#             stack.append(s[i])
#         for i in range(len(stack)):
#             str.append(stack.pop())
#         return str


#     def reverseStringViaExtendedSlice(self, s):
#         return s[::-1]


#     def reverseStringViaReversed(self, s):
#         return list("".join(reversed(s)))


# s2 = AltenateSolution()
# print(s2.reverseStringIteratively(["h","e","l","l","o"]))
# print(s2.reverseStringViaStack(["h","e","l","l","o"]))
# print(s2.reverseStringViaExtendedSlice(["h","e","l","l","o"]))
# print(s2.reverseStringViaReversed(["h","e","l","l","o"]))