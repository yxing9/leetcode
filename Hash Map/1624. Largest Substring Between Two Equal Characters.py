# 1624. Largest Substring Between Two Equal Characters
# Easy


# my solution, pathrise pair programming 3/22
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hashmap = {}
        longest = -1
        
        for i, c in enumerate(s):
            if c not in hashmap:
                hashmap[c] = i
            else:
                longest = max(longest, i - hashmap[c] - 1)
                
        return longest
# 03/23/2022 01:39