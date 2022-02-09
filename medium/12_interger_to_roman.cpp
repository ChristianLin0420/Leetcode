

#include<iostream>
#include<cstring>
#include<vector>

using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        vector<int> value = {1, 5, 10, 50, 100, 500, 1000};
        vector<string> alphabet = {"I", "V", "X", "L", "C", "D", "M"};
        string result = "";
        int idx = value.size() - 1;

        while (num > 0) {
            int quotient = num / value[idx];

            if (quotient == 4) {
                result += (alphabet[idx] + alphabet[idx + 1]);
                num %= value[idx];
            } else if (quotient == 9) {
                result += (alphabet[idx] + alphabet[idx + 2]);
                num %= value[idx];   
            } else if (quotient >= 5) {
                result += (alphabet[idx + 1]);
                num %= value[idx + 1];
                idx += 2;
            } else {
                while (quotient--)
                    result += alphabet[idx];
                num %= value[idx];
            }

            idx -= 2;
        }

        cout << "result: " << result << endl;
        
        return result;
    }
};

int main() {
    Solution s;
    
    s.intToRoman(58);

    return 0;
}