# 322. Coin Change
# M


# Larry, https://www.youtube.com/watch?v=5zCJX5FVp18
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10 ** 20
        
        has_cache = [False] * (amount + 1)
        cache = [None] * (amount + 1)
        # time complexity
        #  number of inputs * time / input
        
        # amount -> 0 to A, where A is the range of amount 10,000
        # number of inputs: O(A)
        # time per input: O(C)
        #  where C is the number of coins
        
        # space complexity
        #  number of inputs * space / input
        # O(A)
        # space per inputs: O(1)
        def getMin(amount):
            if amount == 0:
                return 0
                
            if has_cache[amount]:
                return cache[amount]
            
            best = INF
            
            for coin in coins:
                if amount >= coin:
                    best = min(best, getMin(amount - coin) + 1)
                    
            has_cache[amount] = True
            cache[amount] = best
            return best
        
        ans = getMin(amount)
        if ans >= INF:
            return -1
        return ans
# 05/21/2022 18:29