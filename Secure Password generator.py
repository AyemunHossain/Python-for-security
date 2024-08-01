import secrets
import string

# Generate a ten-character password with 
# one lowercase character
# one uppercase character
# one digit
# one special character

# Create a secure random generator
sr = secrets.SystemRandom()

# Define character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

# Ensure each required character type is included
password = [
    sr.choice(lowercase),
    sr.choice(uppercase),
    sr.choice(digits),
    sr.choice(special_characters)
]

# Fill the rest of the password length with random characters
remaining_length = 15 - len(password)
all_characters = lowercase + uppercase + digits + special_characters
password += [sr.choice(all_characters) for _ in range(remaining_length)]

# Shuffle the password list to ensure randomness
sr.shuffle(password)

# Convert the list to a string and print the password
print("".join(password))