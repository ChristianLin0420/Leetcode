
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<int> indicators(200001, 0);
        vector< vector<int> > result;

        if (nums.size() >= 3) {
            int max_v = -100000, min_v = 100000;
            for (int i = 0; i < nums.size(); i++) {
                indicators[nums[i] + 100000]++;
                min_v = min(min_v, nums[i]);
                max_v = max(max_v, nums[i]);
            }

            min_v += 100000; max_v += 100000;
            
            for (int i = min_v; i <= 100000; i++) {
                if (indicators[i] > 0) {
                    indicators[i]--;
                    for (int j = i; j <= max_v; j++) {                        
                        if (indicators[j] > 0) {
                            indicators[j]--;
                            int val = i + j;
                            int idx = 300000 - val;
                            if (idx >= i && idx >= j && idx <= 200000 && indicators[idx] > 0) {
                                vector<int> tmp;
                                tmp.push_back(i - 100000);
                                tmp.push_back(j - 100000);
                                tmp.push_back(idx - 100000);
                                result.push_back(tmp);
                            }
                            indicators[j]++;
                        }
                    }
                    indicators[i]++; 
                }
            }
        }

        return result;
    }

    vector<vector<int>> threeSum_leetcode(vector<int>& nums) {
        vector< vector<int> > result;
        
        if (nums.size() >= 3) {
            sort(nums.begin(), nums.end());
            for (int i = 0; i < nums.size() - 2; i++) {
                if (i == 0 || (i > 0 && nums[i] != nums[i - 1])) {
                    int j = i + 1, k = nums.size() - 1, target = 0 - nums[i];

                    while(j < k) {
                        if (nums[j] + nums[k] == target) {
                            vector<int> tmp;
                            tmp.push_back(nums[i]);
                            tmp.push_back(nums[j]);
                            tmp.push_back(nums[k]);
                            result.push_back(tmp);

                            while (j < k && nums[j] == nums[j + 1]) j++;
                            while (j < k && nums[k] == nums[k - 1]) k--;
                            j++; k--;
                        } else if (nums[j] + nums[k] < target) {
                            ++j;
                        } else {
                            --k;
                        }
                    }
                }
            }
        }

        return result;
    }
};

int main() {

    vector<int> test{-1,0,1,2,-1,-4};
    vector<vector<int>> result;
    Solution s;
    result = s.threeSum_leetcode(test);

    for (auto it = result.begin(); it != result.end(); ++it) {
        for (auto t = it->begin(); t != it->end(); t++) {
            cout << *t << " ";
        }
        cout << "\n";
    }

    return 0;
}