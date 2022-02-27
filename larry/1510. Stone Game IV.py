# 1510. Stone Game IV
# Hard




class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        '''
        larry, https://www.youtube.com/watch?v=pheAOCB2xgE
        '''
        # Game Theory
        winnable = [False]
        
        for i in range(1, n + 1):
            j = 1
            
            winnable.append(False)
            while (delta := j * j) <= i:
                if not winnable[i - delta]:
                    winnable[i] = True
                    break
                j += 1
            
        return winnable[n]
# 01/22/2022 14:23



# --- END --- #