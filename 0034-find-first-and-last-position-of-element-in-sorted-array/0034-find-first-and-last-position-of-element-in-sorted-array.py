class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        list2 = [-1, -1]
        if target not in nums:
            return list2
        else:
            list1 = []
            b = 0
            e = 0
            for j in nums:
                if j == target:
                    begin = b
                    for z in nums[::-1]:
                        if z == target:
                            end = len(nums) - e - 1
                            list1.append(begin)
                            list1.append(end)
                            return list1
                        else:
                            e += 1
                else:
                    b += 1