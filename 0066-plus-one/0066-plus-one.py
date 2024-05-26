class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        z = ""
        list1 = []
        for i in digits:
            z += str(i)
        z = int(z)
        z += 1
        for i in str(z):
            list1.append(int(i))
        return list1
