
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        
        if (matrix.empty())
            return 0;
        
        int result = 0;
        int row = matrix.size(), col = matrix[0].size();
        vector<vector<int>> table(row, vector<int>(col, 1)); 
        vector<pair<int, pair<int, int>>> grids;
        
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                grids.push_back({matrix[i][j], {i, j}});
            }
        }
        
        sort(grids.begin(), grids.end());
        reverse(grids.begin(), grids.end());
        
        vector<pair<int, int>> four_dir{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        for (auto grid : grids) {
            int r = grid.second.first, c = grid.second.second;
            
            for (auto dir : four_dir) {
                int _r = r + dir.first;
                int _c = c + dir.second;
                
                if (_r >= row || _c >= col || _r < 0 || _c < 0 || matrix[_r][_c] <= matrix[r][c]) {
                    continue;
                } else {
                    table[r][c] = max(table[r][c], table[_r][_c] + 1);
                }
            }
            
            result = max(result, table[r][c]);
        }
        
        return result;
    }
};