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
int lengthofLL(ListNode* head) {
    int count = 0;
    while(head) head = head->next, count++;
    return count;
}
ListNode* prevtailofLL(ListNode* head,int length) {
    for (int i = 0; i < length - 2; i++) { // runs till the head reaches the previous node to tail
        head = head -> next;
    }
    return head;
}
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        int length = lengthofLL(head);
        if (head == NULL || length == 1) {
            return head;
        }
        k %= length; // This freaking line cost me a fucking hour
        // this means doing k rotations and `k % length` rotations give the same result - hence more efficient

        for(int i = 0; i < k; i++) { // while(k--)
            ListNode* prevtail = prevtailofLL(head, length); // returns the node previous to tail
            ListNode* tail = prevtail->next;
            prevtail -> next = NULL;
            tail -> next = head;
            head = tail;
            tail = prevtail;
        }

        return head;
    }
};