from fractions import Fraction

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        list1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
        list2 = [0,1,2,3,4,5,6,7,8,9]
        a = 0
        c = 1
        numerator = 1
        denominator = 10
        for i in num1[::-1]:
            b = Fraction(numerator, denominator)
            b *= c
            for j in num2[::-1]:
                b *= 10
                temp = list2[list1.index(i)] * list2[list1.index(j)]
                a += temp * b

            c *= 10
        return f"{a}"