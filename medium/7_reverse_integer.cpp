
#include<iostream>
#include <climits>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        int reverse = 0;

        while (x != 0) {
            int remain = x % 10;
            x /= 10;
            
            if (reverse > INT_MAX / 10 || (reverse == INT_MAX / 10 && remain > 7)) return 0;
            if (reverse < INT_MIN / 10 || (reverse == INT_MIN / 10 && remain < -8)) return 0;
            
            reverse = 10 * reverse + remain;
        }

        return reverse;
    }
};