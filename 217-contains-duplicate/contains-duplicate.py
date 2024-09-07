class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for i in nums:
            if i not in set1:
                set1.add(i)
            else:
                return True
        return False
