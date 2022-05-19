
#include<iostream>
#include<vector>

using namespace std;


class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        bool col0 = false, row0 = false;

        for (int i = 0; i < m; ++i) 
            col0 |= (matrix[i][0] == 0);
        
        for (int j = 0; j < n; ++j) 
            row0 |= (matrix[0][j] == 0);

        for (int i = 1; i < m; ++i)
            for (int j = 1; j < n; ++j)
                if (matrix[i][j] == 0)
                    matrix[0][j] = matrix[i][0] = 0;      

        for (int i = 1; i < m; ++i)
            for (int j = 1; j < n; ++j)
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;

        if (row0)
            for (int j = 0; j < n; ++j) 
                matrix[0][j] = 0;

        if (col0)
            for (int i = 0; i < m; ++i) 
                matrix[i][0] = 0;
    }
};