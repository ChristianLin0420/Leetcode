
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>

using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> s;
        int start = 1;
        
        for (int i = 1; i <= path.length(); ++i) {
            if (i == path.length() || path[i] == '/') {
                string p = path.substr(start, i - start);
                
                if (p == "/") 
                    continue;
                
                if (p == "..") {
                    if (!s.empty()) 
                        s.pop_back();
                } else if (p.length() > 0 && p != ".") {
                    s.push_back(std::move(p));
                }
                
                start = i + 1;
            }
        }

        string ans;
        
        for (int i = 0; i < s.size(); ++i)
            ans += "/" + s[i];
        
        return ans.empty() ? "/" : ans;
    }
};