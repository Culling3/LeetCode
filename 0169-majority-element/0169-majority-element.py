class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)/2
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for keys, values in count.items():
            if values > n:
                return keys
            else:
                pass
