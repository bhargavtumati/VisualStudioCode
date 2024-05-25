/*reverse a linked list
Given a linked list of N nodes, your task is to reverse the list.

Input Format:
A singly linked list of N nodes, where N is the number of nodes in the linked list.
The linked list is provided as a sequence of N integer values, where each value represents the val of a node, and nodes are connected in the order they are given.
Output Format:

The reversed linked list as a sequence of integers, now ordered from the last node in the input list to the first.
Input:
LinkedList: 2->7->8->9->10

Output:
Reversed LinkedList: 10 9 8 7 2

Example:

Input:

LinkedList: 1->2->3->4->5->6

Output:
Reversed LinkedList: 6 5 4 3 2 1

Constraints:

1 <= N <= 10^4

*/
#include <iostream>

// Define the ListNode structure
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Define the reverseLinked class
class reverseLinked {
public:
ListNode* Solution(ListNode* head) {
  //Write your code here 
  ListNode* previousnode=nullptr;
  ListNode* currentnode=head;
  ListNode* nextnode=nullptr;
  while(currentnode!=nullptr){
    nextnode=currentnode->next;
      currentnode->next=previousnode;
      previousnode=currentnode;
      currentnode=nextnode;
      head=previousnode;
      
  }
  return head;
}
};

// Driver code
int main() {
    // Create a sample linked list (you need to adapt this part based on your actual linked list)
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);

    // Create an instance of the reverseLinked class
    reverseLinked solution;

    // Reverse the linked list
    ListNode* reversed_head = solution.Solution(head);

    // Print the reversed linked list (you need to adapt this part based on your actual linked list)
    ListNode* temp = reversed_head;
    while (temp) {
        std::cout << temp->val << " ";
        temp = temp->next;
    }
    std::cout << std::endl;

    // Clean up memory (you need to adapt this part based on your actual linked list)
    // ...

    return 0;
}
