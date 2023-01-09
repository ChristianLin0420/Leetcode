class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        dp = [0]*(n+1)
        
        for i in range(1,n+1):
            cur_max = 0
            for j in range(1,min(k,i)+1):
                cur_max = max(cur_max,arr[i-j])
                dp[i] = max(dp[i],dp[i-j] + cur_max*j)
                
        return dp[-1]