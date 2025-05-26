/* structure for a node
class Node {
 public:
  int data;
  Node *next;

  Node(int x){
      data = x;
      next = NULL;
  }
}; */

class Solution {
  public:
    Node* sortedInsert(Node* head, int data) {
        // code here
         Node *curr = head;
        Node *prev = head;
        Node *next = NULL;
        Node *new_node = new Node(data);
  
        
        if(head->data >= data)
        {
            new_node->next = head;
            //head = new_node;
            while(curr)
            {
                next = curr->next;
                if(next == head)
                {
                    curr->next = new_node;
                    head = new_node;
                    return head;
                }
                curr = next;
            }
        }
        while(curr)
        {
            next = curr->next;
            if(curr->data < data and next == head)
            {
                
                curr->next = new_node;
                new_node->next = next;
                return head;
            }
            else if(curr->data >= data)
            {
                new_node->next = curr;
                prev->next = new_node;
                return head;
            }
            prev = curr;
            curr = next;
        }
    }
};