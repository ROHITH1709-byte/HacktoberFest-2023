def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b  # Returning a float to avoid losing precision

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))  # Allowing float inputs for better precision
        except ValueError:
            print("Please enter a valid number.")

def user_choice():
    while True:
        print("Calculator Menu:")
        print("1. Addition")
        print("2. Multiplication")
        print("3. Subtraction")
        print("4. Division")
        print("5. Quit")

        user_input = input("Enter your choice (1-5): ")
        
        if user_input.isdigit():
            user_input = int(user_input)
            
            if 1 <= user_input <= 5:
                if user_input == 5:
                    print("Exiting the calculator. Goodbye!")
                    break

                a = get_number("Enter the first number: ")
                b = get_number("Enter the second number: ")

                if user_input == 1:
                    print("Result:", add(a, b))
                elif user_input == 2:
                    print("Result:", mul(a, b))
                elif user_input == 3:
                    print("Result:", sub(a, b))
                elif user_input == 4:
                    result = div(a, b)
                    print("Result:", result)
                    if result == "Division by zero is not allowed":
                        print("Note: Division by zero is not allowed.")
            else:
                print("Please enter a number between 1 and 5.")
        else:
            print("Please enter a valid number.")

user_choice()

