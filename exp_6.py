# Input from user
text = input("Enter a string: ")

# Initialize an empty string to store the reversed version
reversed_text = ""

# Loop through the original string in reverse order
for char in text:
    reversed_text = char + reversed_text  # prepend each character

# Output the result
print("Reversed string:", reversed_text)
