class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        @cache
        def dp(index, bought):
            if index == n:
                return 0

            option1 = option2 = 0

            if not bought:
                option1 = -prices[index] + dp(index + 1, True)
            else:
                option2 = prices[index] - fee + dp(index + 1, False)

            option3 = dp(index + 1, bought)

            return max(option1, option2, option3)

        return dp(0, False)