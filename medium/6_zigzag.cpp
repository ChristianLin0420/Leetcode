
#include<iostream>
#include<cstring>
#include<vector>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {

        if (numRows == 1) {
            return s;
        }

        int slen = s.length();
        char convertedS[1000] = {'\0'};
        
        int factor = 2 * numRows - 2;
        int scan_count = slen / factor + 2;
        unsigned int counter = 0;

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < scan_count; j++) {

                if (counter == slen) {
                    break;
                }

                int idx = i + factor * j;
                
                if (i == 0 || i == numRows - 1) {
                    if (idx < slen) {
                        convertedS[counter++] = s[idx];
                    }
                } else {
                    if (j == 0) {
                        convertedS[counter++] = s[idx];
                    } else {
                        if (idx - i * 2 < slen) {
                            convertedS[counter++] = s[idx - i * 2];
                            if (idx < slen) {
                                convertedS[counter++] = s[idx];
                            }
                        }
                    }
                }
            }
        }

        return string(convertedS);
    }

    // Leetcode solution //
    string convert1(string s, int numRows) {

        if (numRows == 1) return s;

        vector<string> rows(min(numRows, int(s.size())));
        int curRow = 0;
        bool goingDown = false;

        for (char c : s) {
            rows[curRow] += c;
            if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
            curRow += goingDown ? 1 : -1;
        }

        string ret;
        for (string row : rows) ret += row;
        return ret;
    }
};

int main() {

    string s = "ABCDE";
    int numberRows = 4;

    Solution solution;
    string newS = solution.convert(s, numberRows);

    cout << newS << endl;

}