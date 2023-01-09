class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def helper(i):
            if i == len(nums) - 1:
                res.append(nums.copy())
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                helper(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        helper(0)

        return res