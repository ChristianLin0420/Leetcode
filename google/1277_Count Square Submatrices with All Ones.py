class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r > 0 and c > 0:
                    if matrix[r][c-1] and matrix[r-1][c-1] and matrix[r-1][c] and matrix[r][c]:
                        matrix[r][c] = min(matrix[r][c-1], matrix[r-1][c-1], matrix[r-1][c]) + 1
                
                count += matrix[r][c]

        return count


