# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
# Ask user to input
# Remove spaces then print
whitespace = 0
text = str(input("Enter your name with spaces in the beginning: "))
if whitespace < len(text):
    text = text.replace(" ", "")

print(text)