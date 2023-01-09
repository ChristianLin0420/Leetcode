class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        nsub = 0
        g    = 1
        
        # the idea is to add new numbers to the last subarray that 
        # results in the non-increase of GCD; 
        # once we hit 1, a new subarray is created
        for n in nums:
            g = gcd(n,g)
            if g == 1:
                nsub += 1
                g = n
        
        return nsub