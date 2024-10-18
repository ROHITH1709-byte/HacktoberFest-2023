#include <iostream>
using namespace std;

void printSpaces(int count) {
    for (int j = 0; j < count; j++) {
        cout << " ";
    }
}

void printStars(int count) {
    for (int j = 0; j < count; j++) {
        cout << "*";
    }
}

void printDiamond(int n) {
    // Upper part of the diamond
    for (int i = 1; i <= n; i += 2) {
        printSpaces((n - i) / 2);
        printStars(i);
        cout << endl;
    }
    
    // Lower part of the diamond
    for (int i = n - 2; i >= 1; i -= 2) {
        printSpaces((n - i) / 2);
        printStars(i);
        cout << endl;
    }
}

int main() {
    int n;

    cout << "Enter the number of rows (should be an odd number): ";
    while (true) {
        cin >> n;

        // Input validation
        if (cin.fail() || n <= 0) {
            cin.clear(); // Clear the error flag
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
            cout << "Invalid input. Please enter a positive odd number: ";
            continue;
        }

        if (n % 2 == 0) {
            cout << "Please enter an odd number for a symmetric diamond pattern." << endl;
            cout << "Try again: ";
            continue;
        }

        break; // Valid input received
    }

    printDiamond(n);

    return 0;
}
