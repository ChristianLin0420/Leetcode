
#include<iostream>
#include<vector>
#include <climits>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int len = nums.size();
        vector<int> counter(len, 0);

        for (int i = len - 2; i >= 0; i--) {
            int tmp = INT_MAX - 1;
            
            for (int j = 1; j <= nums[i]; j++) {
                if (i + j < len) tmp = min(tmp, counter[i + j]);
                else break;
            }

            counter[i] = tmp + 1;
        }

        return counter[0];
    }
};