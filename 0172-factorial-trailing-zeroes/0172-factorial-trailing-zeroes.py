import sys
sys.set_int_max_str_digits(999999999)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        n1 = n
        list1 = []
        z = 1
        o = 0
        for i in range(n - 1):
            n1 -= 1
            list1.append(n1 + 1)
        for i in list1:
            z *= i
        z = str(z)
        for i in z[::-1]:
            if i == "0":
                o += 1
            else:
                break
        return o