# 394. Decode String
# Medium


'''

12/19/2021
I don't know what's category / topics of problem is. => stack, recursion
    recursion because there can be nested []


Key steps:
1. go to the deepest brackets and start from there
2. identify the number k, then append [content] k times to output array
   If there are letters not in [], append them one time to output array, 
   in other words, only letters in [] need to be multiplied k times

*numbers k must be followed by []


What I learned from this question:
My thought was correct after I was hinted "stack" in lc discuss. 

The direction of my original code was correct. 

But a long way to go and a lot to learn in Python if I want to write bug-free code in Python, 
or any other language. 


'''

# my original solution - failed
class Solution:
    def decodeString(self, s: str) -> str:
        s = list(s)
        stack = []
        temp = []
        res = []
        
        for i in s:
            if i == ']':
                while stack.pop() != '[': # keep popping content off [] until hit a [
                    temp.append(stack.pop()) # add content to temp
                stack.pop() # pop off '['
                k = stack.pop() # set k
                while k > 0:
                    res += [temp]
                    k -= 1
            else:
                stack.append(i)
                
        return res
# Runtime Error
# IndexError: pop from empty list
#     temp.append(stack.pop())
# Line 11 in decodeString (Solution.py)
#     ret = Solution().decodeString(param_1)
# Line 39 in _driver (Solution.py)
#     _driver()
# Line 50 in <module> (Solution.py)
'''

Look back at this code, 
1. I didn't know I can process str directly
2. I didn't know I only needed one stack as the output array
3. temp has the same function as substr
4. Don't use stack.pop() where it should stack[-1]
5. I didn't know add at front of a list can be a = b + a
6. I didn't know .isdigit() to check if a str is a digit
7. I didn't know multiply a string multiple times can be "k * substr"

'''


# https://www.youtube.com/watch?v=qB0zZpBJlh8
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
                
            else:
                substr = ""
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop() # pop off '['
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * substr)
                
        return "".join(stack)
# Runtime: 32 ms, faster than 58.89%
# time:       O(maxK ** countK * n)
# space: O(sum(maxK ** countK * n))



# --- End --- #