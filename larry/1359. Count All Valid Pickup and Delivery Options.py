# 1359. Count All Valid Pickup and Delivery Options
# Hard


# Larry, https://www.youtube.com/watch?v=Q0dVILwk-dY
class Solution:
    def countOrders(self, N: int) -> int:
        MOD = 10 ** 9 + 7
        # OEIS -> look that up

        # N = 1
        # P1, D1

        # N = 2
        # X X
        # 3 + 2 + 1 = 6 * f(1) = 6

        # N = 3
        # X X X X
        # 5 + 4 + 3 + 2 + 1 = 15 * f(2) = 15 * 6 = 90

        # N = 4
        # P X X X X X X
        # 7 + 6 + 5 + .. + 1 =  28 * f(3) = 28 * 90 = 2520
        ans = 1

        for i in range(2, N + 1):
            previous = (2 * (i - 1))
            pickup = previous + 1
            total = (pickup * (pickup + 1)) // 2
            current = ans * total
            current %= MOD
            ans = current
        
        return ans % MOD
# 03/06/2022 15:40