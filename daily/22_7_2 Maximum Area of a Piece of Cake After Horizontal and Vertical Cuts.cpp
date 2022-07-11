
#include<iostream>
#include<vector>
#include<cstring> 
#include<algorithm>

using namespace std;

class Solution {
public:
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
        int mod = 1e9 + 7;
        
        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(), verticalCuts.end());
 
        horizontalCuts.push_back(h);
        verticalCuts.push_back(w);
        
        int maxHorizontal = horizontalCuts[0];
        int maxVertical = verticalCuts[0];
 
        for (int i = 1; i < horizontalCuts.size(); i++) {
            int diff = horizontalCuts[i] - horizontalCuts[i - 1];
            maxHorizontal = max(maxHorizontal, diff);
        }
 
        for (int i = 1; i < verticalCuts.size(); i++) {
            int diff = verticalCuts[i] - verticalCuts[i - 1];
            maxVertical = max(maxVertical, diff);
        }
 
        return (int)((long)maxHorizontal * maxVertical % mod);
    }
};