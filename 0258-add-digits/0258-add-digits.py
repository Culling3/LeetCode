class Solution:
    def addDigits(self, x: int) -> int:
        if 0 <= x <= (2**31 - 1):
            if len(str(x)) == 1:
                return x
            else:
                while True:
                    list1 = []
                    for i in str(x):
                        list1.append(i)
                    x = 0
                    for i in list1:
                        x += int(i)
                    if len(str(x)) == 1:
                        return x
                    else:
                        pass

        else:
            return None