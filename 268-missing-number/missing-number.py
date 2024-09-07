class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        z = 0
        if min(nums) != 0:
            return 0
        while True:
            if z == nums[z]:
                pass
            else:
                return z
            z += 1
            if len(nums) == z:
                return z 