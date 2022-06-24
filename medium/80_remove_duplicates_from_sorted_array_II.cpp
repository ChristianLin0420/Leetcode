
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        int cur = nums[0], count = 1, total_count = 0;
        
        for(int i = 1; i < nums.size(); i++) {
            if (nums[i] == cur) {
                if (count < 2) {
                    count++;
                } else {
                    total_count++; 
                    nums[i] = 10001;
                }
            } else {
                cur = nums[i];
                count = 1;
            }
        }
        
        sort(nums.begin(), nums.end());
        
        return nums.size() - total_count;
    }
};