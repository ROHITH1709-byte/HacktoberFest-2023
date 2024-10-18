#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node *next;

    Node(int val) : data(val), next(nullptr) {} // Constructor to initialize the node
};

Node* Insert(int pos, int x, Node* head) {
    Node* t = new Node(x); // Create new node

    if (pos == 0) {
        t->next = head;
        return t; // New head
    } else {
        Node* p = head;
        for (int i = 0; i < pos - 1 && p; i++) {
            p = p->next;
        }
        if (p) {
            t->next = p->next;
            p->next = t;
        } else {
            delete t; // Position is out of bounds
            cout << "Position is out of bounds." << endl;
        }
    }
    return head;
}

void Display(Node* head) {
    Node* p = head;
    while (p) {
        cout << p->data << " ";
        p = p->next;
    }
    cout << endl; // New line after displaying the list
}

bool Loop(Node* head) {
    if (!head) return false; // No nodes in the list

    Node *slow = head, *fast = head;

    while (fast && fast->next) {
        slow = slow->next; // Move slow pointer by 1
        fast = fast->next->next; // Move fast pointer by 2

        if (slow == fast) { // Loop detected
            return true;
        }
    }
    return false; // No loop
}

int main() {
    Node* first = nullptr;
    int x, n;

    cout << "Enter the number of elements you want to enter: ";
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        cin >> x;
        first = Insert(i, x, first);
    }

    // Display the linked list
    cout << "Linked List: ";
    Display(first);

    // Check for loop
    if (Loop(first))
        cout << "Linked List has a loop." << endl;
    else
        cout << "Linked List does not have a loop." << endl;

    // Memory cleanup
    Node* current = first;
    while (current) {
        Node* nextNode = current->next;
        delete current; // Free allocated memory
        current = nextNode;
    }

    return 0;
}
