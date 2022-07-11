
#include<iostream>
#include<vector>
#include<cstring> 
#include<algorithm>

using namespace std;

class Solution {
public:
    int fib(int n) {
        if (val[n] != -1) {
            return val[n];
        } else {
            if (n == 0) val[n] = 0;
            else if (n == 1) val[n] = 1;
            else val[n] = fib(n - 1) + fib(n - 2);
            return val[n];
        }
    }
private:
    vector<int> val{31, -1};
};