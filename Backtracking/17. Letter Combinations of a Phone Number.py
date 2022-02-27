# 17. Letter Combinations of a Phone Number
# Medium


# DFS

# 09/11/2021
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/1197410/python-simple-dfs-easy-to-unsterstand.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = len(digits)
        if l == 0:
            return []
        
        mp = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        
        def dfs(digits, cur, pos):
            if pos == l:
                res.append(cur)
                return 
            for i in mp[digits[pos]]:                
                dfs(digits, cur+i, pos+1)
        
        dfs(digits, "", 0)
        return res
# time: O(3^n) 3 because 3 child nodes. n is len(digits)
# space: 


#04122021
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

# Train of Thoughts
# digits can be as long as 4 numbers -> use recursion
# Below is the essential part of the function before recursion.
# NB: anything recursive can be implemented iteratively, i.e., without recursion
'''
result = []
l2 = ['a','b','c']
l3 = ['d','e','f']
l4 = ['g','h','i']
l5 = ['j','k','l']
digits = '23'

for i in l2:
    for j in l3:
        for k in l4:
            for l in l5:
                result.append(i+j+k+l)
print(result)
'''

# Approach 1:
class Solution:
    def letterCombinations(digits):
        l2 = ['a','b','c']
        l3 = ['d','e','f']
        l4 = ['g','h','i']
        l5 = ['j','k','l']
        l6 = ['m','n','o']
        l7 = ['p','q','r','s']
        l8 = ['t','u','v']
        l9 = ['w','x','y','z']
        
        result = ['']

        if len(digits) == 0:
            return result

        for i in range(len(digits)):
            if digits[i] == '2':
                for letter in l2:
                    result.append(letter)
        # or 
        while ct < len(digits):
            if digits[ct] == '2':
                for b in l2:
                    result.append(b)
                    ct += 1
# Code Abandoned
# There is one thing I cannot overcome with this approach:
# for letter in l2:
#   for i in result:
#       result.append(i+letter)
# The only way is through result.append(i+j+k+l) where i,j,k,l is not an element in result
# I can't add/concatenate an element that is already in a list to the same list
res = []
digits = '23'

mp = {'2':['a','b','c'],'3':['d','e','f'],'4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

for i in range(len(digits)):
    if digits[i] in mp:
        for letter in mp[digits[i]]:
            res.append(letter)
print(res)
# output: ['a', 'b', 'c', 'd', 'e', 'f']
# This is the same as what I got before at line 77. Still need to deal with combinations.

# Referring to solutions
# What I think the hardest part of this problem: Dealing with combinations using recursion.
# How they solve it:
# combinations.append(''.join(path))


# I wrote after reading a  solution:
class Solution:
    def letterCombinations(self, digits):
        
        if len(digits) == 0:
            return []
        
        mp = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        # This is where I did wrong. See line 141.
        # index = 0
        # path = []

        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append(''.join(path))
                return
                # Do not forget this return, this is the only return in backtrack()
            # This if condition glues combinations together.

            possible_letters = mp[digits[index]]
            # for i in range(len(digits)):
            # No need to have the above line, since index in backtrack() takes care of the iteration.
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path) # key
                path.pop() # key
                # Why pop the last to avoid "index out of range" error?
                # We need path.pop() to make the index oscillate between 0 and 1, for example when digits = '23'. But Why?
                # Why when we do not pop 'd', index will move to 2?
                # Because we need pop to break/exit the for loop from time to time by letting len(path) == len(digits)
                # to reset index to 0
            # This for loop is where the combinations magic happens.
            # backtrack(index +1, path) is equal to another for loop, thus equals
            # for i in l2:
            #   for j in l3:
            #       result.append(i+j)
            # no matter how many l4, l5, l6 are in there

        combinations = []
        backtrack(0, [])
        # Remember when writing recursion, you need to call the recursive function to initiate the recursion.
        return combinations

'''
The key is to understand this part and know the sequence of execution.

def backtrack(index, path):
    if len(path) == len(digits):
        combinations.append(''.join(path))
        return 
            
    possible_letters = mp[digits[index]]
    for letter in possible_letters:
        path.append(letter)
        backtrack(index + 1, path)
        path.pop()

    combinations = []
    backtrack(0, [])

It is a loop inside another loop, like Inception. 
1st execution: line 156. print path = ['a']
2nd execution: line 157 + new line 156. print path = ['a', 'd']
3rd execution: new line 157 + first-time line 151 and return. print combinations = ['ad'] and path = ['a', 'd']
4th execution: first-time line 158. path = ['a']
    line 158 pops because line 157 finishes 'd' as the the first round of iteration in digits[1],
    and exits backtrack(index + 1, path)
'''
# 如何理解path.pop()：
# 第一个加入path的a不会被pop因为path.append()在path.pop()之前
# a在pop之前会经历一次backtrack(index+1,path)
# a因此会变成['a','d']，合并并加入combinations
# 此时a会被pop，重新变成['a']

# solution code: backtrack
'''
def letterCombinations(digits):
        
    if len(digits) == 0:
        return []
        
    mp = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

    def backtrack(index, path):
        if len(path) == len(digits):
            combinations.append(''.join(path))
            return

        possible_letters = mp[digits[index]]

        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path) # key
            path.pop() # key

    combinations = []
    backtrack(0, [])

    return combinations
    
print(letterCombinations('23')) -> ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
'''