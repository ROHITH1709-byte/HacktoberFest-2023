import java.util.Scanner;
import java.util.Random;

public class GuessTheNumber {
    public static void main(String[] args) {
        Random random = new Random();
        int generatedNumber = random.nextInt(101); // Generates a number between 0 and 100
        System.out.println("Generated Number: " + generatedNumber); // For debugging purposes
        
        Scanner input = new Scanner(System.in);
        System.out.println("Number Generated Successfully!!\n\nNow start Guessing the Number.");
        System.out.println("Are you ready? Enter Yes or No.");
        String response = input.next();

        if (response.equalsIgnoreCase("yes")) {
            int attempts = 0;
            boolean gameOn = true;

            while (gameOn) {
                System.out.println("Make a Guess:");
                int userGuess = input.nextInt();
                attempts++;

                if (userGuess < generatedNumber) {
                    System.out.println("Oops!! Not a right guess. \nHint: Increase your number.");
                } else if (userGuess > generatedNumber) {
                    System.out.println("Oops!! Not a right guess. \nHint: Decrease your number.");
                } else {
                    System.out.println("Congrats!! You guessed it right.");
                    break; // Exit loop on correct guess
                }

                System.out.println("Number of attempts: " + attempts);
                System.out.println("Do you want to continue? Enter Y for Yes or N for No.");
                String continueResponse = input.next();
                if (continueResponse.equalsIgnoreCase("n")) {
                    gameOn = false; // Exit game if user chooses not to continue
                }
            }
        } else {
            System.out.println("Game cancelled.");
        }

        input.close(); // Close the scanner to avoid resource leaks
    }
}
