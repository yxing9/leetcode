# 953. Verifying an Alien Dictionary
# Easy

'''

两个两个来比较

'''

from typing import List


'''

words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
             i      i




isLeftSmaller won't work

isLeftLarger works


Why?
Maybe because we should rule out all False first.
'''


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        dic = {}
        
        for index, val in enumerate(order):
            dic[val] = index
        
        def isLeftLarger(word1, word2):
            nonlocal dic
            m, n = len(word1), len(word2)
            for i in range(min(m, n)):
                if word1[i] != word2[i]:
                    if dic[word1[i]] > dic[word2[i]]:
                        return True
                    else:
                        return False
            return m > n

        for i in range(n):
            if i + 1 == n: return True
            word1, word2 = words[i], words[i+1]
            if isLeftLarger(word1, word2):
                return False
        return True
# Runtime: 36 ms, faster than 75.07% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 14.3 MB, less than 72.69%



# Below is isLeftSmaller
# The only changes are flipping the direction of <
# and flipping True and False
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        dic = {}
        
        for index, val in enumerate(order):
            dic[val] = index
        
        def isLeftSmaller(word1, word2):
            nonlocal dic
            m, n = len(word1), len(word2)
            for i in range(min(m, n)):
                if word1[i] != word2[i]:
                    if dic[word1[i]] < dic[word2[i]]:
                        return True
                    else:
                        return False
            return m < n

        for i in range(n):
            if i + 1 == n: return True
            word1, word2 = words[i], words[i + 1]
            if isLeftSmaller(word1, word2):
                return True
        return False





# Wrong pathrise version?
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        dic = {}
        
        for i, c in enumerate(order):
            dic[c] = i
        
        def isLeftLarger(word1, word2):
            nonlocal dic
            m, n = len(word1), len(word2)
            for i in range(min(m, n)):
                if word1[i] != word2[i]:
                    if dic[word1[i]] > dic[word2[i]]:
                        return True
                    else:
                        return False
            return m > n    # "apple", "app"

        for i in range(n):
            if i + 1 == n: return True
            word1, word2 = words[i], words[i + 1]
            if isLeftSmaller(word1, word2):
                return True
        return False


s = Solution()
print(s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")) # expect True
print(s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")) # expect False
print(s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")) # expect False