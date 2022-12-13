import random

def generate_password(length, include_lowercase, include_uppercase, include_numbers, include_symbols):
  # Start with an empty password
  password = ""

  # Define a string of all the possible characters we want to include in the password
  possible_characters = ""
  if include_lowercase:
    possible_characters += "abcdefghijklmnopqrstuvwxyz"
  if include_uppercase:
    possible_characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  if include_numbers:
    possible_characters += "0123456789"
  if include_symbols:
    possible_characters += "!@#$%^&*()_+-=[]{}|:;<>,.?/~`"

  # If the possible_characters string is empty, there are no character types selected
  # In this case, we return an empty string
  if len(possible_characters) == 0:
    return ""

  # Generate the password by selecting random characters from the possible_characters string
  for i in range(length):
    password += random.choice(possible_characters)

  # Return the generated password
  return password

# Generate a password that is 10 characters long and includes lowercase letters, uppercase letters, and numbers
password = generate_password(10, True, True, True, False)

# Print the generated password
print(password)
