# Read the contents of input.txt
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

# Count the number of words in the file
word_count = sum(len(line.split()) for line in lines)

# Convert all text to uppercase
processed_lines = [line.upper() for line in lines]

# Write the processed text and the word count to output.txt
with open('output.txt', 'w') as outfile:
    outfile.writelines(processed_lines)
    outfile.write(f"\nTotal words: {word_count}\n")

# Print success message
print("output.txt has been created successfully.")
