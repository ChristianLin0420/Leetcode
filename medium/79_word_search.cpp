
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        row = board.size(), col = board[0].size();
        
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if(search(board, word, 0, r, c)) 
                    return true;
            }
        }
        
        return false;
    }
    
    bool search(vector<vector<char>> &board, string& word, int d, int x, int y) {
        if(x < 0 || x == row || y < 0 || y == col || word[d] != board[x][y]) 
            return false;
        
        // Found the last char of the word
        if(d == word.length() - 1)
            return true;
        
        char cur = board[x][y];
        board[x][y] = 0; 
        bool found = search(board, word, d + 1, x + 1, y)
                  || search(board, word, d + 1, x - 1, y)
                  || search(board, word, d + 1, x, y + 1)
                  || search(board, word, d + 1, x, y - 1);
        board[x][y] = cur;
        return found;
    }
private:
    int row;
    int col;
};