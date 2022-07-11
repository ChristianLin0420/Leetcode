
#include<iostream>
#include<vector>
#include<cstring> 
#include<algorithm>

using namespace std;


class Solution {
public:
    int minDeletions(string s) {
        vector<int> frequency(26, 0);
        int deletion = 0;
        
        for (auto& c : s) {
            frequency[c - 'a']++;
        }
        
        sort(frequency.begin(), frequency.end());
                
        for(int i = 24; i >= 0; i--) {
            if (frequency[i] == 0) break;
            if (frequency[i] >= frequency[i + 1]) { 
                while(frequency[i] >= frequency[i + 1] && frequency[i] > 0) {
                    frequency[i]--; 
                    deletion++;
                } 
            }
        }
        
        return deletion;
    }
};