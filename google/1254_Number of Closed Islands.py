class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    island_count += self.countIsland(grid, i, j)
        return island_count
    
    def countIsland(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == 0:
                grid[i][j] = 1
                return  (self.countIsland(grid, i-1, j) * self.countIsland(grid, i, j-1)
                    * self.countIsland(grid, i+1, j) * self.countIsland(grid, i, j+1))
            return 1
        return 0