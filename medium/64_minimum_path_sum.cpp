
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int row = grid.size(), col = grid[0].size();
        
        for(int i = 0; i < row; i++) {
            for(int j = 0; j < col; j++) {
                if(i - 1 < 0) {
                    if(j - 1 < 0) continue;
                    else grid[i][j] += grid[i][j - 1];
                } else if (j - 1 < 0) {
                    grid[i][j] += grid[i - 1][j];
                } else {
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]);
                }
            }
        }
        
        return grid[row - 1][col - 1];
    }
};