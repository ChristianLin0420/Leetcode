class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        pq = [(-grid[0][0], 0, 0)]
        grid[0][0] = -1 # mark as visited 

        while pq: 
            v, i, j = heappop(pq)

            if i == m-1 and j == n-1: 
                return -v
                
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and 0 <= grid[ii][jj]: 
                    vv = min(-v, grid[ii][jj])
                    heappush(pq, (-vv, ii, jj))
                    grid[ii][jj] = -1
        