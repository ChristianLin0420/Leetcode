
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        sort(candidates.begin(), candidates.end());

        for (int i = 0; i < candidates.size(); ++i) {
            if (candidates[i] > target) 
                break;

            if (candidates[i] == target) {
                res.push_back({candidates[i]}); 
                break;
            }

            vector<int> vec = vector<int>(candidates.begin() + i, candidates.end());
            vector<vector<int>> tmp = combinationSum(vec, target - candidates[i]);

            for (auto a : tmp) {
                a.insert(a.begin(), candidates[i]);
                res.push_back(a);
            }
        }

        return res;
    }
};