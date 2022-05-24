
#include<iostream>
#include<vector>
#include<queue>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        priority_queue<int> value;
        vector<int> results;
        
        for(auto num : nums) 
            value.push(num);
        
        for(int i = nums.size() - 1; i >= 0; i--) {
            nums[i] = value.top();
            value.pop();
        }
    }
};