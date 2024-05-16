class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        list1 = []
        list2 = []
        list3 = []
        for i in nums:
            if i not in list1:
                list1.append(i)
            else:
                list2.append(i)
        for i in nums:
            if i in list2:
                pass
            else:
                list3.append(i)
        return int(f"{list3}".replace("[", "").replace("]", ""))