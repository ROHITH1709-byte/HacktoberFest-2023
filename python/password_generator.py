import random

def password_generator(password_lengths):
    data_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@$^&**_"
    passwords_list = [] 
    
    for length in password_lengths:
        password = ''.join(random.choice(data_string) for _ in range(length))
        passwords_list.append(password) 
        
    return passwords_list

def main():
    n = int(input("Number of passwords to generate: "))
    print('Generating', n, 'PASSWORDS')
    
    password_lengths = []
    
    for i in range(n):
        print('NOTE==> Minimum length of password is 6!')
        while True:
            try:
                length = int(input(f'Enter the length of password {i + 1}: '))
                if length < 6:
                    print('Length too short. Setting length to 6.')
                    length = 6
                password_lengths.append(length)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    passwords = password_generator(password_lengths)
    
    for i in range(n):
        print(f'Password {i + 1} = {passwords[i]}')

if __name__ == "__main__":
    main()

