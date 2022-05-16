
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
        if(matrix.empty() || matrix[0].empty())
            return {};
        
        vector<int> result;
        int row = matrix.size(), col = matrix[0].size();
        int up = 0, down = row - 1, left = 0, right = col - 1;
        
        while(true) {
            for(int c = left; c <= right; c++)
                result.push_back(matrix[up][c]);
            if(++up > down) 
                break;
            for(int r = up; r <= down; r++)
                result.push_back(matrix[r][right]);
            if(left > --right)
                break;
            for(int c = right; c >= left; c--)
                result.push_back(matrix[down][c]);
            if(up > --down)
                break;
            for(int r = down; r >= up; r--)
                result.push_back(matrix[r][left]);
            if(++left > right)
                break;
        }
        
        return result;
    }
};