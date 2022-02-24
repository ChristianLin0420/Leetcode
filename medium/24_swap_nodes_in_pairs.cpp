
#include<iostream>

using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        } 

        ListNode* next = head -> next;
        
        if(head -> next != nullptr) {
            head -> next = next -> next;
            next -> next = head;
            head -> next = swapPairs(head -> next);
        } else {
            return head;
        }

        return next;
    }
};