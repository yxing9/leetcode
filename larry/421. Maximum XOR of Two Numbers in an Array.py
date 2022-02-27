# 421. Maximum XOR of Two Numbers in an Array
# Medium



# larry, https://www.youtube.com/watch?v=A76P_30UO38, 29:09
class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None
        
    """
    def hasZero(self):
        return self.zero is not None
        
    def goZero(self):
        if self.zero is None:
            self.zero = TrieNode()
        return self.zero
        
    def hasOne(self):
        return self.one is not None
        
    def goOne(self):
        if self.one is None:
            self.one = TrieNode()
        return self.one
    """
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # O(32) -> O(1) -> O(alpha) where alpha is the number of bits -> 32
    def add(self, number):
        current = self.root
        
        p = pow(2, 31)
        for _ in range(32):
            if (number & p) > 0:
                if current.one is None:
                    current.one = TrieNode()
                current = current.one
            else:
                if current.zero is None:
                    current.zero = TrieNode()
                current = current.zero
            
            p //= 2
    
    # O(32) -> O(1) -> O(alpha) where alpha is the number of bits -> 32
    def findMax(self, number):
        current = self.root
        ans = 0
        
        p = pow(2, 31)
        for _ in range(32):
            if (number & p) > 0:
                # if this bit is 1, then we want to find a zero
                if current.zero is not None:
                    current = current.zero
                else:
                    current = current.one
                    # is we're using the "1", then update answer
                    ans += p
            else:
                # if this bit is 0, then we want to find a one
                if current.one is not None:
                    current = current.one
                    ans += p
                else:
                    current = current.zero
                    
            p //= 2
            
        # ans now contains the number which would produce the max
        return ans ^ number
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        
        best = 0
        # O(N) iterations
        for x in nums:
            # O(32) or O(1)
            trie.add(x)
            best = max(best, trie.findMax(x))
        return best



# --- END --- #