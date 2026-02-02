import random
import string

# Taking user input for password length
length = int(input("Enter desired password length: "))

# Define characters to use in password
letters = string.ascii_letters      # a-z and A-Z
digits = string.digits              # 0-9
symbols = string.punctuation        # special characters

# Combine all characters
all_characters = letters + digits + symbols

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_characters)

# Display generated password
print("Generated Password:", password)
