
#include<iostream>
#include<vector>
#include<climits>
#include<algorithm>

using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());

        int target_d = INT_MAX;
        int target_c = 0;

        for (int i = 0; i < nums.size(); i++) {
            int left = i + 1, right = nums.size() - 1;

            while (left < right) {
                int temp = nums[i] + nums[left] + nums[right];
                int temp_d = (int)abs(temp - target);

                if (temp_d < target_d) {
                    target_d = temp_d;
                    target_c = temp;
                }

                if (temp < target) {
                    left++;
                } else if (temp > target) {
                    right--;
                } else if (temp == target) {
                    return target;
                }
            }
        }

        return target_c;
    }
};

int main() {
    Solution s;
    
    vector<int> tmp = {-1,2,1,-4};
    int solution = s.threeSumClosest(tmp, 1);

    cout << solution << endl;

    return 0;
}