#include <iostream>
#define SIZE 5 // Size of Circular Queue

using namespace std;

class Queue {
private:
    int items[SIZE], front, rear;

public:
    Queue() {
        front = -1;
        rear = -1;
    }

    // Check if the queue is full
    bool isFull() {
        return (front == 0 && rear == SIZE - 1) || (front == rear + 1);
    }

    // Check if the queue is empty
    bool isEmpty() {
        return front == -1;
    }

    // Adding an element
    void enQueue(int element) {
        if (isFull()) {
            cout << "Queue is full" << endl;
        } else {
            if (front == -1) {
                front = 0; // Initialize front when first element is added
            }
            rear = (rear + 1) % SIZE; // Circular increment
            items[rear] = element;
            cout << "Inserted " << element << endl;
        }
    }

    // Removing an element
    int deQueue() {
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return -1;
        } else {
            int element = items[front];
            if (front == rear) {
                front = -1; // Queue is now empty
                rear = -1;
            } else {
                front = (front + 1) % SIZE; // Circular increment
            }
            return element;
        }
    }

    void display() {
        if (isEmpty()) {
            cout << "Empty Queue" << endl;
        } else {
            cout << "Front -> " << front << endl;
            cout << "Items -> ";
            int i = front;
            while (true) {
                cout << items[i] << " ";
                if (i == rear) break; // Exit loop when rear is reached
                i = (i + 1) % SIZE; // Circular increment
            }
            cout << endl << "Rear -> " << rear << endl;
 

