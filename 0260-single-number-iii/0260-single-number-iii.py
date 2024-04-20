class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = {}
        for num in nums:
            if num in a:
                a[num] += 1
            else:
                a[num] = 1

        return [num for num in a if a[num] == 1]