class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_index = nums.index(max(nums))
        return max_index