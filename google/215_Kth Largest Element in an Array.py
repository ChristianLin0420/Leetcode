class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hashmap  = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        minimum_element = min(nums)
        maximum_element = max(nums)

        sample = []

        for i in range(minimum_element,maximum_element+1):
            if i not in hashmap:
                continue
            else:
                frequency = hashmap[i]
                value = i
                sample += [value]*frequency

        return sample[-k]