# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
# Ask user to input anything
# Convert to lower case

text = str(input("Enter whatever: "))
text = text.swapcase()

print(text)