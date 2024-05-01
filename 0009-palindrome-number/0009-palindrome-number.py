class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x1 = x[::-1]
        if x == x1:
            return True
        else:
            return False