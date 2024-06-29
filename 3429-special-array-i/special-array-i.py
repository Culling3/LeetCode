def oddeven(x):
    if x % 2 == 0:
        return 1
    else:
        return 0


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        a = len(nums)
        if a >= 3:
            for i in range(1,(a - 1)):
                if (oddeven(nums[i]) != oddeven(nums[i - 1])) and (oddeven(nums[i]) != oddeven(nums[i + 1])):
                    pass
                else:
                    return False
            return True
        elif a == 1:
            return True
        else:
            if oddeven(nums[0]) != oddeven(nums[1]):
                return True
            else:
                return False