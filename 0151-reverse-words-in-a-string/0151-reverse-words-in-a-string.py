class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s1 = s.split(" ")
        s1 = s1[::-1]
        while "" in s1:
            s1.remove("")
        z = 0
        a = ""
        for i in s1:
            z += 1
            if z != len(s1):
                a += f"{i}"
                a += " "
            else:
                a += f"{i}"
        return a