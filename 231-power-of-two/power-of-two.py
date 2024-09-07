class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        while int(n) > 1:
            n /= 2
            if n == 1:
                return True
        return False