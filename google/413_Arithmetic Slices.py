class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return 0
        
        counter = [0] * len(nums)
        cur_delta = nums[1] - nums[0]

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == cur_delta:
                counter[i] = counter[i - 1] + 1
            else:
                cur_delta = nums[i] - nums[i - 1]

        return sum(counter)
