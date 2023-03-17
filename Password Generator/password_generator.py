import random

# Define a function to generate a password with the given length
def generate_password(length):
    # Define the characters that can be used in the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?~`"
    # Initialize an empty string to store the password
    password = ""
    # Generate the password by randomly selecting characters from the defined set
    for i in range(length):
        password += random.choice(characters)
    # Return the generated password
    return password

# Ask the user for the desired length of the password
password_length = int(input("Enter the desired length of your password: "))

# Generate the password and print it to the console
password = generate_password(password_length)
print("Your generated password is:", password)
