class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        contains_0 = False
        contains_multiple_0 = False
        for n in nums:
            if n != 0:
                total *= n
            elif n==0 and contains_0:
                contains_multiple_0 = True
            else:
                contains_0 = True
        
        res = []
        if contains_0:
            for n in nums:
                if n!=0:
                    res.append(0)
                elif contains_multiple_0:
                    res.append(0)
                else:
                    res.append(total)
        else:
            for n in nums:
                res.append(total//n)
        
        return res