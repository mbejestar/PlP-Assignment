# Ask the user for the filename to read
filename = input("Enter the filename to read: ")

try:
    # Try opening the file for reading
    with open(filename, 'r') as infile:
        content = infile.read()

    # Modify the content (for example, convert to uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    output_filename = "modified_" + filename
    with open(output_filename, 'w') as outfile:
        outfile.write(modified_content)

    print(f"Modified content has been written to {output_filename}")

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
