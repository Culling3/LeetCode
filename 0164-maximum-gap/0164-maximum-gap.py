class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        list1 = []
        nums = sorted(nums)
        if len(nums) >= 2:
            for i in range(len(nums)):
                if (i + 1)!= len(nums):
                    list1.append(abs(nums[i] - nums[i + 1]))
                else:
                    break
            a = max(list1)
            return a
        else:
            return 0
