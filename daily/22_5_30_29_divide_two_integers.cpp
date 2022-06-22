
#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        int sign = (dividend >= 0 ^ divisor >= 0) ? -1 : 1;
        long long int quotient = 0;
        long long int sum = 0;
        
        long long int dividendL = dividend;
        dividendL = abs(dividendL);
        long long int divisorL = divisor;
        divisorL = abs(divisorL);
        
        for (int i = 31; i >= 0; i--) {
            if (sum + (divisorL << i) <= dividendL) {
                sum += (divisorL << i);
                quotient += (1LL << i);
            }
        }
        
        if (sign * quotient > INT_MAX)
            return INT_MAX;
            
        
        return sign * quotient;
    }
};