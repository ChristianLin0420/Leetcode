class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 1
        increse_counter = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increse_counter[i] = increse_counter[i-1] + 1
                
            count += increse_counter[i]

        return count
