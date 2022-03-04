# 799. Champagne Tower
# Medium



# Larry, https://www.youtube.com/watch?v=fJ7qLFuoidk
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        next_row = []
        
        for i in range(1, query_row + 1):
            next_row = []
            
            for j in range(i + 1):
                current = 0
                if j != 0:
                    current += max((row[j - 1] - 1) / 2, 0)
                if j != i:
                    current += max((row[j] - 1) / 2, 0)
                next_row.append(current)
            row = next_row
            
        return min(row[query_glass], 1.0)
# 03/04/2022 15:10