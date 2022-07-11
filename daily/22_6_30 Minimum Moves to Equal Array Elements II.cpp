
#include<iostream>
#include<vector>
#include<cstring> 
#include<algorithm>

using namespace std;


class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int res = 0, i = 0, j = (int)nums.size() - 1;
        sort(nums.begin(), nums.end());
        
        while (i < j) {
            res += nums[j--] - nums[i++];
        }
        
        return res;
    }
};