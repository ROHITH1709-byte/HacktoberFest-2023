

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def main():
    try:
        # Get the temperature in Celsius from the user
        celsius = float(input("Enter the temperature in Celsius: "))
        
        # Convert Celsius to Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)

        # Display the result
        print(f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
