class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        row = len(matrix)
        col = len(matrix[0])

        for r in range(row - 2, -1, -1):
            for c in range(col):
                cur_min = 100000

                if c - 1 >= 0:
                    cur_min = min(cur_min, matrix[r][c] + matrix[r + 1][c - 1])
                
                cur_min = min(cur_min, matrix[r][c] + matrix[r + 1][c])

                if c + 1 < col:
                    cur_min = min(cur_min, matrix[r][c] + matrix[r + 1][c + 1])
                
                matrix[r][c] = cur_min

        return min(matrix[0])