# 22. Generate Parentheses
# Medium
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtracking(pars, openUsed, closeUsed, n):
            if openUsed > n:
                return
            if closeUsed > openUsed:
                return
            if len(pars) == n * 2:
                res.append(pars)
            else:
                backtracking(pars+"(", openUsed+1, closeUsed, n)
                backtracking(pars+")", openUsed, closeUsed+1, n)
        res = []
        backtracking("", 0, 0, n)
        return res
# 63.95%
'''
Pathrise's Balanced Strings solution:

def balancedStrings(n):
    backtracking("", 0, 0, n)
def backtracking(pars, openUsed, closeUsed, n):
    if openUsed > n: return
    if closeUsed > openUsed: return
    if len(pars) == 2*n:
        print(pars)
    else:
        backtracking(pars+'(', openUsed+1, closeUsed, n)
        backtracking(pars+')', openUsed, closeUsed+1, n)
'''