class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        if len(nums1) % 2 == 0:
            a = int(len(nums1)/2) - 1
            b = int(len(nums1)/2 + 1) - 1
            return ((nums1[a] + nums1[b]) / 2)
        else:
            a = int(len(nums1)/2 + 0.5) - 1
            return nums1[a]