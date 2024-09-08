class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        list1 = [0]
        g = set(list1)
        z = 0
        for i in range(len(nums)):

            try:
                if nums[i] + 1 == nums[i + 1]:
                    z += 1
                elif nums[i] == nums[i + 1]:
                    pass
                else:
                    g.add(z + 1)
                    z = 0
            except:
                g.add(z + 1)
                z = 0
        return max(g)