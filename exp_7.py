import random
import string

def generate_long_code(length):
    # Define the characters to choose from (letters and digits)
    characters = string.ascii_letters + string.digits
    # Randomly select characters to form a code of the given length
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

# Get the desired length from the user
length = int(input("Enter the length of the code you want: "))

# Generate and display the code
long_code = generate_long_code(length)
print("Generated Long Code:", long_code)
