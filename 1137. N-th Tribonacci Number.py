class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 0
        if n == 0 or n == 1:
            return n

        for i in range(2, n):
            d = a + b + c
            a = b
            b = c
            c = a
        return c
