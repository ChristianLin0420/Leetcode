
#include<iostream>
#include<vector>
#include<cstring>
#include<map>

using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> ans{""};
        vector<vector<char>> d(10);

        d[0] = {' '};
        d[1] = {};
        d[2] = {'a','b','c'};
        d[3] = {'d','e','f'};
        d[4] = {'g','h','i'};
        d[5] = {'j','k','l'};
        d[6] = {'m','n','o'};
        d[7] = {'p','q','r','s'};
        d[8] = {'t','u','v'};
        d[9] = {'w','x','y','z'};
    
        for (char digit : digits) {
            vector<string> tmp;
            for (const string& s : ans)
               for (char c : d[digit - '0'])
                    tmp.push_back(s + c);
            ans.swap(tmp);
        }
        
        return ans;
    }
};