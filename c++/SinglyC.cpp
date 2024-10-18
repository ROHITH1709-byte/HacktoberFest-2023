#include <iostream>
using namespace std;

template<class T>
struct node {
    T iNo;
    struct node* next;
};

template<class T>
class SinglyC {
private:
    int iSize;
    node<T>* Head;
    node<T>* Tail;

public:
    SinglyC();
    void InsertFirst(T);
    void InsertLast(T);
    void InsertAtPos(int, T);
    void DeleteFirst();
    void DeleteLast();
    void DeleteAtPos(int);
    void Display();
    int Count();
};

template<class T>
SinglyC<T>::SinglyC() {
    Head = nullptr;
    Tail = nullptr;
    iSize = 0;
}

template<class T>
void SinglyC<T>::InsertFirst(T iNo) {
    node<T>* newn = new node<T>;
    newn->iNo = iNo;
    newn->next = nullptr;

    if (Head == nullptr && Tail == nullptr) {
        Head = newn;
        Tail = newn;
    } else {
        newn->next = Head;
        Head = newn;
    }
    Tail->next = Head;
    iSize++;
}

template<class T>
void SinglyC<T>::InsertLast(T iNo) {
    node<T>* newn = new node<T>;
    newn->iNo = iNo;
    newn->next = nullptr;

    if (Head == nullptr && Tail == nullptr) {
        Head = newn;
        Tail = newn;
    } else {
        Tail->next = newn;
        Tail = newn;
    }
    Tail->next = Head;
    iSize++;
}

template<class T>
void SinglyC<T>::InsertAtPos(int iPos, T iNo) {
    if (iPos < 1 || iPos > (iSize + 1)) {
        cout << "Unable to insert an element! Please provide a valid position!" << endl;
        return;
    } else if (iPos == 1) {
        InsertFirst(iNo);
    } else if (iPos == (iSize + 1)) {
        InsertLast(iNo);
    } else {
        node<T>* newn = new node<T>;
        newn->iNo = iNo;
        newn->next = nullptr;

        node<T>* temp = Head;
        for (int i = 1; i < iPos - 1; i++) {
            temp = temp->next;
        }

        newn->next = temp->next;
        temp->next = newn;
        iSize++;
    }
}

template<class T>
void SinglyC<T>::DeleteFirst() {
    if (Head == nullptr) {
        cout << "No elements found to delete from the linked list!" << endl;
        return;
    } else if (Head == Tail) {
        delete Head;
        Head = nullptr;
        Tail = nullptr;
    } else {
        node<T>* temp = Head;
        Head = Head->next;
        delete temp;
    }
    Tail->next = Head;
    iSize--;
}

template<class T>
void SinglyC<T>::DeleteLast() {
    if (Head == nullptr) {
        cout << "No elements found to delete from the linked list!" << endl;
        return;
    } else if (Head == Tail) {
        delete Head;
        Head = nullptr;
        Tail = nullptr;
    } else {
        node<T>* temp = Head;
        while (temp->next != Tail) {
            temp = temp->next;
        }
        delete Tail;
        Tail = temp;
        Tail->next = Head;
    }
    iSize--;
}

template<class T>
void SinglyC<T>::DeleteAtPos(int iPos) {
    if (iPos < 1 || iPos > iSize) {
        cout << "Unable to delete an element! Please provide a valid position!" << endl;
        return;
    } else if (iPos == 1) {
        DeleteFirst();
    } else if (iPos == iSize) {
        DeleteLast();
    } else {
        node<T>* temp = Head;
        for (int i = 1; i < iPos - 1; i++) {
            temp = temp->next;
        }
        node<T>* temp1 = temp->next;
        temp->next = temp1->next;
        delete temp1;
    }
    iSize--;
}

template<class T>
void SinglyC<T>::Display() {
    node<T>* temp = Head;

    if (temp == nullptr) {
        cout << "List is empty" << endl;
        return;
    } else {
        do {
            cout << "|" << temp->iNo << "|->";
            temp = temp->next;
        } while (temp != Head);
        cout << "NULL" << endl;
    }
}

template<class T>
int SinglyC<T>::Count() {
    return iSize;
}

int main() {
    SinglyC<int> lobj;

    lobj.InsertFirst(1);
    lobj.InsertFirst(2);
    lobj.InsertFirst(3);
    lobj.InsertFirst(4);
    lobj.InsertFirst(5);
    lobj.Display();

    lobj.InsertLast(0);
    lobj.InsertLast(-1);
    lobj.InsertLast(-2);
    lobj.Display();

    cout << "The total number of elements present in the linked list: " << lobj.Count() << endl;

    lobj.InsertAtPos(2, 10);  // Corrected the position
    lobj.Display();

    lobj.DeleteFirst();
    lobj.Display();

    lobj.DeleteLast();
    lobj.Display();

    lobj.DeleteAtPos(6);  // Will give error as there are only 6 elements now
    lobj.Display();

    return 0;
}
