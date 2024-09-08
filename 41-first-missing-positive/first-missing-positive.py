class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a = set(nums)
        z = 1
        while True:
            if z in a:
                pass
            else:
                return z
            z += 1