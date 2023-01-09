class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        dp = [[0] * (maxCoupons+1) for _ in range(maxAmount+1)]
        n, ans = len(price), 0

        for idx in range(n):
            for i in range(maxAmount, -1, -1):
                for j in range(maxCoupons, -1, -1):
                    if i - price[idx] >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - price[idx]][j] + tastiness[idx])
                        
                    if j > 0 and i - price[idx] // 2 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - price[idx] // 2][j-1] + tastiness[idx])
                        
                    ans = max(ans, dp[i][j])

        return ans