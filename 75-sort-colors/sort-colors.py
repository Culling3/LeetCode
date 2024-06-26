class Solution:
    def sortColors(self, nums: List[int]) -> None:
        list1 = []
        for i in nums:
            if i == 0:
                list1.append(i)
        for i in nums:
            if i == 1:
                list1.append(i)
        for i in nums:
            if i == 2:
                list1.append(i)

        for i in range(len(nums)):
            nums[i] = list1[i]