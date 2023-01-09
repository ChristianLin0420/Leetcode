class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        stack = [([], nums)]
        
        res = [[]]
        
        while stack:
            perm, candidates = stack.pop()
            
            for i in range(len(candidates)):
                
                new_per = perm + [candidates[i]]
                new_can = candidates[:i]
                
                stack.append([new_per, new_can])
                res.append(new_per)
        
        return res