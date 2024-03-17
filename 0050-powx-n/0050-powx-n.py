class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (-100.0 < x < 100.0) and ((-2**31) <= n <= (2**31)-1) and (-10**4 <= x**n <= 10**4) and (x != 0              or n > x) and (type(n) == int):
            return x**n
        else:
            pass