# 9. Palindrome Number
# Easy


# my initial solution
# convert str to int + two pointers
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        N = len(x)
        l, r = 0, N - 1
        
        while l < r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        
        return True
# 01/25/2022 18:46
# time O(N), N is str(x).length
# space O(1)

# ----------------------------------------------------------------------------------------

# my 2nd solution
# reverse an integer
# without converting the input int to str
# reference: https://www.geeksforgeeks.org/write-a-program-to-reverse-digits-of-a-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        def reverseInteger(n):
            rev = 0
            
            while n > 0:
                rev = rev * 10 + n % 10
                n //= 10
                
            return rev
        
        return x == reverseInteger(x)
# 01/25/2022 18:58
# time O(log N), N is the input integer
# space O(1)



# There is at least a 3rd solution using str reverse and list(), "".join()
# just see below
'''

x = 125
x = str(x)
x = list(x)
x.reverse()
print(x)
print("".join(x))
print(type("".join(x)))
print(int("".join(x)))
print(type(int("".join(x))))

just too much back and forth

'''


# from LC Solution section
# convert to str then reverse the string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
# 01/25/2022 19:08





# --- END --- #