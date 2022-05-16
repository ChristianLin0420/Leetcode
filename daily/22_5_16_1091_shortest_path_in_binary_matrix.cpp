
#include<iostream>
#include<set>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        
        if (grid[0][0] == 1) 
            return -1;
        
        int res = 0;
        int size = grid.size();
        
        set<vector<int>> visited;
        visited.insert({0, 0});
        queue<vector<int>> q;
        
        q.push({0, 0});
        vector<vector<int>> dirs{{-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}};
        
        while (!q.empty()) {
            ++res;
        
            for (int i = q.size(); i > 0; --i) {
                auto t = q.front(); q.pop();
                
                if (t[0] == size - 1 && t[1] == size - 1) 
                    return res;
            
                for (auto dir : dirs) {
                    int col = t[0] + dir[0];
                    int row = t[1] + dir[1];
                    
                    if (col < 0 || col >= size || row < 0 || row >= size || grid[col][row] == 1 || visited.count({col, row})) 
                        continue;
                    
                    visited.insert({col, row});
                    q.push({col, row});
                }
            }
        }
        
        return -1;
    }
};