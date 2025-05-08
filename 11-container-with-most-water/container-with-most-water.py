class Solution:
    def maxArea(self, height: List[int]) -> int:
        list1 = []
        max1 = 0
        i = 0
        j = len(height) - 1
        while True:
            if height[i] < height[j]:
                area = (j - i) * height[i]
                i += 1
            else:
                area = (j - i) * height[j]
                j -= 1
            if area > max1:
                max1 = area
            if j == i:
                return max1      