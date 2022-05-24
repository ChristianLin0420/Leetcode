
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> table(m + 1, vector<int>(n + 1, 0));
        
        for(string s : strs) {
            int zero = 0, one = 0;
            
            for(char c : s) {
                if (c == '0') zero++;
                else one++;
            }
            
            for(int i = m; i >= zero; i--) {
                for(int j = n; j >= one; j--) {
                    table[i][j] = max(table[i][j], table[i - zero][j - one] + 1);
                }
            }
        }
        
        return table[m][n];
    }
};