#include <iostream>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};
void printList(ListNode* head) {
    while (head) {
        std::cout << head->val << " ";
        head = head->next;
    }
    std::cout << std::endl;
}
class NodeCombi {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == NULL) return l2;
        if(l2 == NULL) return l1;
        if(l1->val > l2->val) 
        std::swap(l1 , l2);
        ListNode *res = l1;
        
        while(l1 != NULL && l2 != NULL ){
            ListNode *temp = NULL;
            while(l1!=NULL && l1->val<=l2->val){
                temp = l1;
                l1 = l1->next;
            }
            temp->next=l2;
            std::swap(l1,l2);
        }
        
        return res;
    }
};

int main(){
  ListNode* n1 = new ListNode(0);//nullptr
    //n1->next = new ListNode(2);
    //n1->next->next = new ListNode(4);
    //n1->next->next->next = new ListNode(6);
    //n1->next->next->next->next = new ListNode(8);

    ListNode* n2 = new ListNode(1);
 n2->next = new ListNode(3);
    n2->next->next = new ListNode(5);
    n2->next->next->next = new ListNode(7);
    n2->next->next->next->next = new ListNode(9);
    NodeCombi nc;
   printList(nc.mergeTwoLists(n1,n2));


    
    
}
