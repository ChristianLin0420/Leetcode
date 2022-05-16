
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<vector<int>> count(m, vector<int>(n, 0));
        
        if(obstacleGrid[0][0] == 1) 
            return 0;
        
        for(int i = 0; i < m; i++) {
            if(obstacleGrid[i][0] == 1) break;
            else count[i][0] = 1;
        }
        
        for(int i = 0; i < n; i++) {
            if(obstacleGrid[0][i] == 1) break;
            else count[0][i] = 1;
        }
        
        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 0)
                    count[i][j] = count[i - 1][j] + count[i][j - 1];
            }
        }
        
        return count[m - 1][n - 1];
    }
};