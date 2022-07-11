
#include<iostream>
#include<vector>
#include<cstring> 
#include<algorithm>

using namespace std;

class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(), [](vector<int> a, vector<int> b) {
            return a[1] > b[1];
        });
            
        int result = 0;
            
        for(int i = 0; i < boxTypes.size(); i++) {
            if (truckSize == 0) {
                return result;
            } else if (truckSize < boxTypes[i][0]) {
                return (result + boxTypes[i][1] * truckSize);
            } else {
                result += boxTypes[i][0] * boxTypes[i][1];
                truckSize -= boxTypes[i][0];
            }
        }
        
        return result;
    }
};