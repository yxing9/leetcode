# 1009. Complement of Base 10 Integer
# Easy
# bit manipulation
# 476. Number Complement


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        todo, bit = n, 1
        while todo:
            n = n ^ bit
            bit  = bit << 1
            todo = todo >> 1
        return n
# 01/03/2022 19:12
# time O(1)
# space O(1)



# --- End --- #