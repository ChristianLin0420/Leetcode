
#include<iostream>
#include<vector>
#include<queue>

using namespace std;

class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int n = heights.size();        
        priority_queue<int, vector<int>, greater<int>> q;
        
        for (int i = 1; i < n; ++i) {
            int d = heights[i] - heights[i - 1];
            if (d <= 0) continue;
            q.push(d);
            if (q.size() <= ladders) continue;
            bricks -= q.top(); 
            q.pop();
            if (bricks < 0) return i - 1;      
        }
        return n - 1;
    }
};