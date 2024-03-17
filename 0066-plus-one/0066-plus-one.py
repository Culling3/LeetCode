class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list1 = []
        a = ""
        for i in digits:
            a += str(i)
        a = int(a)
        a += 1
        a = str(a)
        for i in a:
            list1.append(int(i))
        return list1