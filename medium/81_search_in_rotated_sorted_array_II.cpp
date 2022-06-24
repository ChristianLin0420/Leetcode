
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        if (target == nums[0]) {
            return true;
        } else if (target > nums[0]) {
            for(int i = 1; i < nums.size(); i++) {
                if (target == nums[i]) {
                    return true;
                } else if (i + 1 < nums.size()) {
                    if (target < nums[i + 1] || nums[i] > nums[i + 1])
                        return false;
                }
            }
        } else {
            for(int i = nums.size() - 1; i > 0; i--) {
                if (target == nums[i]) {
                    return true;
                } else if (i - 1 >= 0) {
                    if (target > nums[i - 1] || nums[i] < nums[i - 1])
                        return false;
                }
            }
        }
        
        return false;
    }
};