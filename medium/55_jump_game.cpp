
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        vector<bool> success(nums.size(), false);
        success[nums.size() - 1] = true;
        
        for(int i = nums.size() - 2; i >= 0; i--) {            
            for(int j = 1; j <= nums[i]; j++) {
                if (success[i + j] == true) {
                    success[i] = true;
                    break;
                }
            }
            
            if(success[i] == false && i == 0) return false;
        }
        
        return true;
    }
};