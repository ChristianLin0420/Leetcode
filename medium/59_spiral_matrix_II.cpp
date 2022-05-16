
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> matrix(n, vector<int>(n, 0));
        int up = 0, down = n - 1, left = 0, right = n - 1;
        int count = 1;
        
        while(true) {
            for (int c = left; c <= right; c++) matrix[up][c] = count++;
            if (++up > down) break;
            for (int r = up; r <= down; r++) matrix[r][right] = count++;
            if (--right < left) break;
            for (int c = right; c >= left; c--) matrix[down][c] = count++;
            if (--down < up) break;
            for (int r = down; r >= up; r--) matrix[r][left] = count++;
            if (++left > right) break;
        }
        
        return matrix;
    }
};