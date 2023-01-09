class Solution:

    def __init__(self, w: List[int]):
        self.accumulate = list(accumulate(w))

    def pickIndex(self) -> int:
        return bisect_left(self.accumulate, random.randint(1, self.accumulate[-1]))
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()