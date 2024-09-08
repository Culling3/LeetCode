def conv(x):
    b = ""
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    if x == "" or x[0] not in nums:
        return 0
    for i in range(len(x)):
        if x[i] in nums:
            b += x[i]
        else:
            return b
    return b


def bit32(y):
    y = int(y)
    if -2147483648 <= y <= 2147483647:
        if y < 0:
            y = str(y)
            y = y.replace("-", "")
            return y
        else:
            return y
    else:
        if y < 0:

            return 2147483648
        elif y > 0:
            return 2147483647
        

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0
        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        g = s[0]
        if g in nums:
            c = conv(s)
            c = bit32(c)
            return c
        elif g == "+":
            s = s.replace("+", "", 1)
            c = conv(s)
            c = bit32(c)
            return c
        elif g == "-":
            s = s.replace("-", "", 1)
            c = conv(s)
            c = bit32(f"-{c}")
            return int(f"-{c}")
        else:
            return 0