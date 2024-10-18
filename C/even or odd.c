/* Program to determine even or odd */

#include <stdio.h>

int main(void) {
    int n; // declaring the required variable

    printf("Enter an integer: ");  // prompt user for input
    scanf("%d", &n);  // store the user input in a variable

    // Check whether the entered number is even or odd
    if (n % 2 == 0) {
        printf("%d is an even number!\n", n);
    } else {
        printf("%d is an odd number!\n", n);
    }

    return 0; // end of main
}
