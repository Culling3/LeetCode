class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        io = 0
        for i in range(len(nums)):
            ko = 0
            io += 1
            for k in range(len(nums)):
                ko += 1
                if ko == io:
                    pass
                elif nums[i] + nums[k] == target:
                    return [i, k]
                else:
                    pass