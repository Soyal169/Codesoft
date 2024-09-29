import random
import string

def generate_password(length):
    # All possible characters for the password (letters, digits, and punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by randomly choosing characters
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# User input: Ask for the desired length of the password
length = int(input("Enter the desired length for the password: "))

# Generate the password
generated_password = generate_password(length)

# Display the password
print("Generated Password: ", generated_password)
