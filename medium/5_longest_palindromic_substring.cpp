
#include<iostream>
#include<cstring>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int table[1001][1001] = {false};
        
        for(int i = 0; i < s.size(); i++) {
            table[i][i] = true;

            if (i < s.size() - 1) 
                table[i][i + 1] = (s[i] == s[i + 1]);
        }

        for(int i = 2; i < s.size(); i++) {

            for(int j = 0; j + i < s.size(); j++) {
                table[j][j + i] = (s[j] == s[j + i] && table[j + 1][j + i - 1]);
            }
        }

        int max_len = 0;
        string max_len_substring = s.substr(0, 1);

        for(int i = 0; i < s.size(); i++) {
            for(int j = i; j < s.size(); j++) {
                if (table[i][j]) {
                    if (j - i > max_len) {
                        max_len = j - i;
                        max_len_substring = s.substr(i, j - i + 1);
                    }
                }
            }
        }

        return max_len_substring;
    }
};