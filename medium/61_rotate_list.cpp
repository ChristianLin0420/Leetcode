
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) 
            return NULL;
        
        int len = 1;
        ListNode *cur = head;
        
        while (cur -> next) {
            ++len;
            cur = cur -> next;
        }
        
        cur -> next = head;
        int m = len - k % len;
        
        for (int i = 0; i < m; ++i) 
            cur = cur -> next;
        
        ListNode *newhead = cur->next;
        cur->next = NULL;
        
        return newhead;
    }
};