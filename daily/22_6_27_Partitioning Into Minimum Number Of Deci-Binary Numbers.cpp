
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>

using namespace std;

class Solution {
public:
    int minPartitions(string n) {
        char best = '0';
        for (auto& c : n)
            if (c > best) best = c;
        return best - '0';
    }
};