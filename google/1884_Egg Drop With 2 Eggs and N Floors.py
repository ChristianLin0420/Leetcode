class Solution:
    def twoEggDrop(self, n: int) -> int:
        start,step = 1,1
        while n > start:
            step += 1
            start += step
        return step