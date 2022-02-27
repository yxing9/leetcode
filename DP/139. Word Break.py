# 139. Word Break
# Medium



# DP Memo
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        memo = {}
        return self.wordBreakMemo(s, wordDict, 0, memo)

    def wordBreakMemo(self, s, wordDict, startIndex, memo):
        if startIndex == len(s):
            return True

        if startIndex in memo:
            return memo[startIndex]

        for endIndex in range(startIndex+1, len(s)+1):
            if s[startIndex:endIndex] in wordDict:
                if self.wordBreakMemo(s, wordDict, endIndex, memo):
                    memo[startIndex] = True
                    return memo[startIndex]
            
        memo[startIndex] = False
        return memo[startIndex]
# time: 
# space:





# Brute force: recursive backtracking aka DFS -> TLE
class Solution:
    def wordBreak(self, s, wordDict, startIndex=0) -> bool:
        if startIndex == len(s):
            return True
        for endIndex in range(startIndex+1, len(s)+1):
            currentWord = s[startIndex:endIndex]
            if currentWord in wordDict:
                if self.wordBreak(s, wordDict, endIndex):
                    return True
        return False
'''

"leetcode"
["leet","code"]
"applepenapple"
["apple","pen"]
"catsandog"
["cats","dog","sand","and","cat"]

"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

'''
