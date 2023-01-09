class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        difference = sorted([n1 - n2 for n1, n2 in zip(nums1, nums2)])

        left = 0
        right = len(difference) - 1
        result = 0

        while left < right:
            if difference[left] + difference[right] > 0:
                result += right - left
                right -= 1
            else:
                left += 1

        return result