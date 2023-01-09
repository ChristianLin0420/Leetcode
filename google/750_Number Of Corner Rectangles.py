class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:

        ans = 0
        d = defaultdict(int)
        for i in range(len(grid)):
            for a, b in itertools.combinations([j for j in range(len(grid[0])) if grid[i][j]], 2):
                ans += d[a, b]
                d[a, b] += 1
        return ans 