# 134. Gas Station
# Medium




class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        larry, https://www.youtube.com/watch?v=NjEQ1qD-SlY&t=17s
        '''
        N = len(gas)
        
        gas = gas + gas
        cost = cost + cost
        
        start = 0
        current = 0
        
        for i, (g, c) in enumerate(zip(gas, cost)):
            next_current = current + g - c
            
            if next_current < 0:
                start = i + 1
                current = 0
            else:
                current = next_current 
                
            if i - start >= N:
                return start
        return-1
# 01/21/2022 17:45




# --- END --- #