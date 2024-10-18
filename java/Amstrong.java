import java.util.Scanner;

public class Armstrong {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int inputNumber = sc.nextInt();
        int tempNumber = inputNumber;
        int numberOfDigits = 0;

        // Count the number of digits
        while (tempNumber != 0) {
            tempNumber /= 10;
            ++numberOfDigits;
        }

        tempNumber = inputNumber;
        int sum = 0;

        // Calculate the sum of the powers of its digits
        while (tempNumber != 0) {
            int digit = tempNumber % 10;
            sum += Math.pow(digit, numberOfDigits);
            tempNumber /= 10;
        }

        // Output the result
        if (inputNumber == sum) {
            System.out.println(inputNumber + " is an Armstrong number.");
        } else {
            Sy
