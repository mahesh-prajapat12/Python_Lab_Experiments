# Function to reverse each line of a file
def reverse_file_lines(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            # Read all lines from the file
            lines = infile.readlines()

        # Open the output file in write mode
        with open(output_filename, 'w') as outfile:
            # Reverse each line and write to the output file
            for line in lines:
                outfile.write(line[::-1])  # Reverse the line and write it

        print(f"Lines have been reversed and saved in {output_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get input and output file names from the user
input_filename = input("Enter the input file name: ")
output_filename = input("Enter the output file name: ")

# Call the function to reverse lines
reverse_file_lines(input_filename, output_filename)
