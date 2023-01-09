class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        stack = []
        result = [-1] * n

        for i in range(n):
            while stack and stack[-1][0] < nums[i]:
                num, j = stack.pop()
                result[j] = nums[i]

            stack.append([nums[i], i])

        if stack:
            for i in range(n):
                while stack and stack[-1][0] < nums[i]:
                    num, j = stack.pop()
                    result[j] = nums[i]

        return result
            