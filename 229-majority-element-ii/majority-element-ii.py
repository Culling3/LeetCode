class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a = len(nums) // 3
        dict1 = {}
        list1 = []

        if a == 0:
            b = set(nums)
            for i in b:
                list1.append(i)
            return list1

        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
                if dict1[i] > a:
                    if i in list1:
                        pass
                    else:

                        list1.append(i)
        return list1