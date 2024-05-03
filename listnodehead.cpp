#include <iostream>

// Definition for singly-linked list
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Function to remove the nth node from the end of the linked list
ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode* fast = head;
    ListNode* slow = head;

    // Move fast pointer n steps ahead
    for (int i = 0; i < n; ++i) {
        fast = fast->next;
    }

    // If fast reached the end, remove the head
    if (!fast) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
        return head;
    }

    // Move both pointers until fast reaches the end
    while (fast->next) {
        fast = fast->next;
         slow = slow->next;
    }

    // Remove the nth node from the end
    ListNode* temp = slow->next;
    slow->next = slow->next->next;
    delete temp;
    return head;
}

// Helper function to print the linked list
void printList(ListNode* head) {
    while (head) {
        std::cout << head->val << " ";
        head = head->next;
    }
    std::cout << std::endl;
}

int main() {
    // Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    int n = 2; // Remove the 2nd node from the end

    std::cout << "Original list: ";
    printList(head);

    head = removeNthFromEnd(head, n);

    std::cout << "List after removing " << n << "th node from the end: ";
    printList(head);

    // Clean up memory
    while (head) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }

    return 0;
}
