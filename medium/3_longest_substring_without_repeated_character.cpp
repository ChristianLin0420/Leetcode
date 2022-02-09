
#include<iostream>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int string_length = s.length();
        
        if (string_length == 0) return 0;
        
        int ascii_table[128] = {0};
        int max_length = 1;
        
        for(int i = 0; i < string_length - 1; i++) {
            
            int length = 1;
            int begin_alphabet_index = int(s[i]);
            ascii_table[begin_alphabet_index] = 1;
            
            for(int j = i + 1; j < string_length; j++) {
                int alphabet_index = int(s[j]);
                
                if (ascii_table[alphabet_index] != 1) {
                    length++;
                    ascii_table[alphabet_index] = 1;
                    max_length = max(length, max_length);
                } else {
                    for (int k = 0; k < 128; k++)
                        ascii_table[k] = 0;
                    
                    max_length = max(length, max_length);
                    break;
                }
            }
        }
        
        return max_length;
    }
};