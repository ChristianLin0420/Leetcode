class Solution:
    def dfs(self, grid, row, col):
        m, n = len(grid), len(grid[0])
        while row < m and col < n:
            if grid[row][col] == 1:
                if (col+1) < n and grid[row][col+1] == 1:
                    row, col = row+1, col+1
                else:
                    return -1
            else:
                if (col-1) > -1 and grid[row][col-1] == -1:
                    row, col = row+1, col-1
                else:
                    return -1
        return col
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        n = len(grid[0])
        for i in range(n):
            ans.append(self.dfs(grid, 0, i))
        return ans