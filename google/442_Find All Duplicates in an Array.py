class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = [0] * len(nums)
        results = []

        for num in nums:
            counter[num - 1] += 1

        for i in range(len(nums)):
            if counter[i] == 2:
                results.append(i + 1)

        return results