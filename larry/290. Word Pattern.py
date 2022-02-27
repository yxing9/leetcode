# 290. Word Pattern
# 



'''

This looks like a very interesting question. 

'''


# Larry's, https://www.youtube.com/watch?v=zT5ennCuo0M
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        lookup = {}
        rlookup = {}
        
        for p, w in zip(pattern, words):
            if p in lookup and lookup[p] != w:
                return False
            if w in rlookup and rlookup[w] != p:
                return False
            
            lookup[p] = w
            rlookup[w] = p
            
        return True
# time O(M + N) M is pattern.length, N is s.length
# space O(M + N) M is pattern.length, N is s.length




# --- END --- #