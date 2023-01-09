class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        pattern = grid[0]
        patternInverse = [x^1 for x in pattern]
        
        for row in grid[1:]:
            if row == pattern or row == patternInverse:
                continue
            else:
                return False
        return True