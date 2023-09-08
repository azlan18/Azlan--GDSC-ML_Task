import string
import secrets

def generate_password(length, use_special_characters):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits

    # Initialize the characters variable based on complexity
    if use_special_characters:
        characters = lowercase_letters + uppercase_letters + digits + string.punctuation
    else:
        characters = lowercase_letters + uppercase_letters + digits

    # Check if length is valid
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for security.")

    # Initialize an empty string to store the password
    password = ''

    # Generate the password by appending 'length' random characters
    for _ in range(length):
        random_character = secrets.choice(characters)
        password += random_character

    return password

# Get user input for password length
while True:
    try:
        length = int(input("Enter password length (at least 8 characters): "))
        break  # Exit the loop if valid input is provided
    except ValueError:
        print("Please enter a valid integer.")

# Get user input for complexity (1 for letters and digits, 2 for letters, digits, and special characters)
while True:
    try:
        complexity = int(input("Enter password complexity (1 for letters and digits, 2 for letters, digits, and special characters): "))
        if complexity not in [1, 2]:
            raise ValueError()
        break
    except ValueError:
        print("Please enter 1 or 2.")

# Generate the password based on user input
use_special_characters = (complexity == 2)
password = generate_password(length=length, use_special_characters=use_special_characters)

print("Generated Password:", password)
