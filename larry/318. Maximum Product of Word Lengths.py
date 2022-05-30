# 318. Maximum Product of Word Lengths
# M


# Larry, https://www.youtube.com/watch?v=aIOtcf8Rc7s
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        
        sets = [None] * N
        lengths = [None] * N
        
        # gets a set of characters of word
        
        # [False, False, False, ..., False]
        # -> FFTFFFFFFFFF
        #      ^
        # -> 0010100100000 = s
        #    0000100000000
        
        def get_set(word):
            s = 0
            for c in word:
                s |= 1 << (ord(c) - ord('a'))
            return s
        
        for i in range(N):
            sets[i] = get_set(words[i])
            lengths[i] = len(words[i])
            
        best = 0
        for i in range(N):
            for j in range(i + 1, N):
                # check whether words[i] and words[j] have common letters
                # 26 * (1000 * 1000 / 2) ~= 13 mil
                
                if (sets[i] & sets[j]) == 0:
                    current = lengths[i] * lengths[j]
                    if current > best:
                        best = current
                        
        return best
# 05/29/2022 13:03