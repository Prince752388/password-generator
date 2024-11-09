import random
import string

def generate_password(length):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices to select random characters for the password
    password = ''.join(random.choices(all_characters, k=length))
    
    return password

def main():
    # Prompt user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 6:  # Minimum length for security reasons
                print("Password length should be at least 6 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
