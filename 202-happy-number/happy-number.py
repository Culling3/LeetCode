def abc(x):
    b = 0
    for i in str(x):
        i = int(i)
        b += i*i
    return b


class Solution:
    def isHappy(self, n: int) -> bool:
        z = []
        while (n != 1):
            n = abc(n)
            if n in z:
                return False
            z.append(n)
            if n == 1:
                return True
            else:
                pass
        if n == 1:
            return True
        return False