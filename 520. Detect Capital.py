# 520. Detect Capital
# Easy


# my solution
# time O(N)
# space O(1)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lower = list(string.ascii_lowercase)
        upper = list(string.ascii_uppercase)
        
        lower_ct = upper_ct = 0
        
        for i in word:
            if i in lower:
                lower_ct += 1
            else:
                upper_ct += 1
                
        N = len(word)
        
        if word[0] in lower and lower_ct != N:
            return False
        if word[0] in upper and upper_ct != 1 and upper_ct < N:
            return False
        
        return True
# 01/24/2022 16:44



# larry, https://www.youtube.com/watch?v=eapVHs-tUks
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or word == word.capitalize()
# 01/24/2022 16:52



# --- END --- #