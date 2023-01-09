def searcher(grid, visited, maxArea):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i,j) not in visited:
                maxArea = max(maxArea, helper(grid, visited, [i,j], [0]))
            
            visited[(i,j)] = 1
        
    return maxArea

def helper(grid, visited, coor, counter):
    counter[0] += 1
    i,j = coor[0], coor[1]
    visited[(i,j)] = 1
    
    # go up if in bounds
    if i > 0:
        if grid[i-1][j] == 1 and (i-1,j) not in visited:
            helper(grid, visited, [i-1, j], counter)
            
    # go down if in bounds
    if i < len(grid) -1:
        if grid[i+1][j] == 1 and (i+1,j) not in visited:
            helper(grid, visited, [i+1,j], counter)
    
    # go left if in bounds
    if j > 0:
        if grid[i][j-1] == 1 and (i,j-1) not in visited:
            helper(grid, visited, [i,j -1], counter)
            
    # go right if in bounds
    if j < len(grid[0]) -1:
        if grid[i][j+1] == 1 and (i,j+1) not in visited:
            helper(grid, visited, [i,j+1], counter)
            
    #return area we got
    return counter[0]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return searcher(grid, {}, 0)