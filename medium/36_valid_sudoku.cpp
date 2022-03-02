
#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // check row
        for (int i = 0; i < 9; i++) {
            vector<int> row_checker(9, 0);
            for(auto i: board[i]) {
                if (i == '.') continue;
                if (row_checker[i - '1'] > 0) return false;
                else row_checker[i - '1']++;
            }
        }

        // check column
        for (int i = 0; i < 9; i++) {
            vector<int> column_checker(9, 0);
            for (int j = 0; j < 9; j++) {
                if (board[j][i] == '.') continue;
                if (column_checker[board[j][i] - '1'] > 0) return false;
                else column_checker[board[j][i] - '1']++;
            }
        }

        // check grid
        for (int round_r = 0; round_r < 3; round_r++) {
            for (int round_c = 0; round_c < 3; round_c++) {
                vector<int> grid_checker(9, 0);
                for (int i = 3 * round_r; i < 3 * (round_r + 1); i++) {
                    for (int j = 3 * round_c; j < 3 * (round_c + 1); j++) {
                        if (board[i][j] == '.') continue;
                        if (grid_checker[board[i][j] - '1'] > 0) return false;
                        else grid_checker[board[i][j] - '1']++;
                    }
                }
            }
        }

        return true;
    }
};