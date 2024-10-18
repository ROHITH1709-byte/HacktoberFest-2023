import java.util.Scanner;

class PalindromeChecker {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a string:");
        String s = sc.nextLine().trim(); // Trim whitespace from both ends

        // Normalize the string to ignore case and non-alphanumeric characters
        String cleaned = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        boolean isPalindrome = true;

        for (int i = 0; i < cleaned.length() / 2; i++) {
            if (cleaned.charAt(i) != cleaned.charAt(cleaned.length() - i - 1)) {
                isPalindrome = false;
                break; // Exit the loop early if not a palindrome
            }
        }

        if (isPalindrome) {
            System.out.println('"' + s + "\" is a palindrome string.");
        } else {
            System.out.println('"' + s + "\" is not a palindrome string.");
        }

        sc.close(); // Close the scanner to prevent resource leaks
    }
}
