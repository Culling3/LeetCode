def check(a):
        if -2**31 - 1 <= a <= 2**31 - 1:
            return a
        else:
            return 0

class Solution:
    def reverse(self, a: int) -> int:
        a = str(a)
        if a[-1] == "0":
            if "-" in a:
                a = a[::-1]
                a = "" + a[1:]
                a = a.replace("-", "")
                a = check(int(a))
                return int(f"-{a}")
            else:
                a = a[::-1]
                if a == "0":
                    return int(a)
                else:
                    a = "" + a[1:]
                    a = check(int(a))
                    return int(a)
        elif "-" in a:
            a = a[::-1]
            a = a.replace("-", "")
            a = check(int(a))
            return int(f"-{a}")
        else:
            a = a[::-1]
            a = check(int(a))
            return int(f"{a}")

    