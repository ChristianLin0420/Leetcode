
#include<iostream>
#include<vector>
#include<stack>
#include<algorithm>

using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        int result = 0, start = 0;
        stack<int> st;
        
        for(int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                st.push(i);
            } else if (s[i] == ')') {
                if (st.empty()) {
                    start = i + 1;
                } else {
                    st.pop();
                    result = st.empty() ? max(i - start + 1, result) : max(i - st.top(), result);
                }
            }
        }
        
        return result;
    }
};