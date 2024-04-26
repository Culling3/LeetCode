import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        x1 = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if x1 == x1[::-1]:
            return True
        else:
            return False

        