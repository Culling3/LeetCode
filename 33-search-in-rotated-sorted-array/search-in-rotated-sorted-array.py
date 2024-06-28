class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i == target:
                return nums.index(i)
            else:
                pass
        return -1