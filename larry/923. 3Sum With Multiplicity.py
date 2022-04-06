# 923. 3Sum With Multiplicity
# Medium


'''

[1,1,2,2,3,3,4,4,5,5], target = 8
 i       j   k

[1,1]
[2,2]
[3,3]
[4,4]
[5,5]

1 + 2 + 5 -> 2 * 2 * 2 = 8
1 + 3 + 4 -> 2 * 2 * 2 = 8
2 + 2 + 4 -> 1 * 1 * 2 = 2
2 + 3 + 3 -> 2 * 1 * 1 = 2
                         20

still have no clue which algorithm or data structure to use

Why return it modulo?
'''


# Larry, https://www.youtube.com/watch?v=d_kAUbR4JVA
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        MAXR = 103
        
        count = [0] * (MAXR)
        
        # O(N)
        for x in arr:
            count[x] += 1
            
        total = 0
        i = target // 3
        if i + i + i == target:
            total += math.comb(count[i], 3)
            total %= MOD
            
        # O(R)
        for i in range(MAXR):
            j = target - i - i
            
            if j != i and j >= 0 and j < MAXR:
                total += (math.comb(count[i], 2) * count[j])
                total %= MOD
            
        # O(R^2)
        for i in range(MAXR):
            for j in range(i + 1, MAXR):
                k = target - i - j
                
                if k > j and k >= 0 and k < MAXR:
                    total += count[i] * count[j] * count[k]
                    total %= MOD
                    
        # O(N + R^2) time
        # O(R) space
        return total % MOD
# 04/06/2022 15:53