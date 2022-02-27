# 3. Longest Substring Without Repeating Characters
# Medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        trueLongesString = ""
    def backtracking(current, remain):
        nonlocal longestString
        if len(remain) == 0 or remain[0] in current:
            longestString = current
            return
        else:
            backtracking(current + remain[0], remain[1:])

        for i in range(0,len(s)):
            longestString = ""
            backtracking("",s[i:])
        if len(longestString) > len(trueLongesString):
            trueLongesString = longestString

        return len(trueLongesString)
'''
this works but it took too long to run so leetcode doesn't accept this answer, so i think the only way to solve this question is using 2 pointers or sliding window.
'''

def longestSubString(str):
    def backtracking(cur, str):
        if str[0] in cur: 
            res.append(cur)
            return
        else:
            backtracking(cur+str[0], str[1:])
    res = []
    backtracking("", str)
    
    return len(res[0])
    
print(longestSubString("abcabcbb"))
#print(longestSubString("abcdefabc"))
