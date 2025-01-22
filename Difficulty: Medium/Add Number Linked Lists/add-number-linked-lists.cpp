//{ Driver Code Starts
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

/* Linked list Node */
struct Node {
    int data;
    struct Node* next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};

Node* buildList() {
    vector<int> arr;
    string input;
    getline(cin, input);
    stringstream ss(input);
    int number;
    while (ss >> number) {
        arr.push_back(number);
    }
    if (arr.empty()) {
        return NULL;
    }
    int val = arr[0];
    int size = arr.size();

    Node* head = new Node(val);
    Node* tail = head;

    for (int i = 1; i < size; i++) {
        val = arr[i];
        tail->next = new Node(val);
        tail = tail->next;
    }

    return head;
}

void printList(Node* n) {
    while (n) {
        cout << n->data << " ";
        n = n->next;
    }
    cout << endl;
}


// } Driver Code Ends
/* node for linked list:

struct Node {
    int data;
    struct Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

*/

class Solution {
  public:
   Node * rev(Node * head){
       Node * prev =NULL;
       while(head){
           Node * next = head->next;
           head->next =prev;
           prev =head;
           head =next;
       }
       return prev;
   }
  
    Node* addTwoLists(Node* num1, Node* num2) {
        // code here
        num1 = rev(num1);
        num2 =rev(num2);
        
        Node * head = new Node(0);
        Node * temp=head;
       int carry=0 ;
       
       while(num1 || num2 || carry){
           int sum = carry;
           
           if(num1){
               sum+=num1->data;
               num1=num1->next;
           }
           if(num2){
               sum+=num2->data;
               num2=num2->next;
           }
           carry = sum/10;
           temp->next = new Node(sum%10);
           temp = temp->next;
           
       }
      head = rev(head->next);
      
       while(head->data==0){
           head=head->next;
       }
       return head;
      
       
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore(); // To ignore the newline character after the integer input

    while (t--) {
        Node* num1 = buildList();
        Node* num2 = buildList();
        Solution ob;
        Node* res = ob.addTwoLists(num1, num2);
        printList(res);
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends