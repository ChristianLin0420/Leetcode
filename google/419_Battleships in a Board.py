class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        row = len(board)
        col = len(board[0])
        count = 0

        visited = [[False] * col for _ in range(row)]

        def traverse_battleship(r, c):
            if c < col - 1:
                for j in range(c+1, col):
                    if board[r][j] == "X":
                        visited[r][j] = True
                    else:
                        break

            if r < row - 1:
                for i in range(r+1, row):
                    if board[i][c] == "X":
                        visited[i][c] = True
                    else:
                        break

        for r in range(row):
            for c in range(col):
                if visited[r][c] or board[r][c] == ".":
                    continue
                else:
                    visited[r][c] = True
                    count += 1
                    traverse_battleship(r, c)

        return count
