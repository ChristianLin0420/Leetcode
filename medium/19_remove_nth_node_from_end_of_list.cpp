
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* res = head;
        ListNode* pre = nullptr;
        ListNode* next = nullptr;

        if (n == 1 && head -> next == nullptr) {
            ListNode* none = nullptr;
            return none;
        } else {
            int over = 1;

            while(over) {
                ListNode* tmp = res;
                int k = n;
                while(k--) tmp = tmp -> next;
                if (tmp == nullptr) {
                    return head -> next;
                } else if (tmp -> next == nullptr) {
                    res -> next = res -> next -> next;
                    over = 0;
                } else {
                    res = res -> next;
                }
            }
        }

        return head;
    }
};

