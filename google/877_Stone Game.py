class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = [[0] * n for i in range(n)]
        
        def dp(i, j):
            if (i > j): return 0
            if (memo[i][j] != 0):
                return memo[i][j]
            
            player_turn = (n - (j - i)) % 2
            if (player_turn == 1):
                # increasing player1's score when player1 picks a max pile
                memo[i][j] = max(piles[i] + dp(i+1, j), piles[j] + dp(i, j-1))
            else:
                # decreasing player1's score when player2 picks a pile and player2 is assumed to pick the larger pile leading to a min score for player1
                memo[i][j] = min(-piles[i] + dp(i+1, j), -piles[j] + dp(i, j-1))
            return memo[i][j]
                
        return dp(0, n-1) > 0