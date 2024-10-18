def is_empty(stk):
    return len(stk) == 0

def push(stk, item):
    stk.append(item)

def pop(stk):
    if is_empty(stk):
        return 'Underflow'
    return stk.pop()

def peek(stk):
    if is_empty(stk):
        return "Underflow"
    return stk[-1]

def display(stk):
    if is_empty(stk):
        print("Stack is empty")
    else:
        print("Stack elements (top to bottom):")
        for item in reversed(stk):
            print(item)

def main():
    stk = []
    while True:
        print("\nStack Operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        try:
            ch = int(input("Enter your choice (1-5): "))
            if ch == 1:
                item = int(input("Enter item to push: "))
                push(stk, item)
                print(f"Pushed {item} to stack.")
            elif ch == 2:
                item = pop(stk)
                if item == 'Underflow':
                    print("Stack is empty, cannot pop.")
                else:
                    print("Popped item is", item)
            elif ch == 3:
                item = peek(stk)
                if item == "Underflow":
                    print("Stack is empty.")
                else:
                    print("Topmost item is", item)
            elif ch == 4:
                display(stk)
            elif ch == 5:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
