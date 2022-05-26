# 1641. Count Sorted Vowel Strings
# M


# Larry, https://www.youtube.com/watch?v=Bpu-A1aZg2w
class Solution:
    def countVowelStrings(self, n: int) -> int:
        has_cache = [[False] * 5 for _ in range(n + 1)]
        cache = [[None] * 5 for _ in range(n + 1)]
        
        # index -> 0 to N
        # last -> 0 to 5
        # total time = number of inputs * time per input
        # number of inputs = 5 * N
        # each input will take = O(1) time
        # in total this will be O(N) times
        def count(index, last):
            if index == n:
                return 1
            
            if has_cache[index][last]:
                return cache[index][last]
            
            total = 0
            for i in range(last, 5):
                total += count(index + 1, i)
                
            has_cache[index][last] = True
            cache[index][last] = total
            return total
        
        total = 0
        for i in range(0, 5):
            total += count(1, i)
        return total
# 05/11/2022 15:43