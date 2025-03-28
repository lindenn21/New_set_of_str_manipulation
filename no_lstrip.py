# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
# Ask user to input
# Remove spaces then print

text = str(input("Enter your name with spaces in the beginning: "))
text = text.replace(" ", "")
print(text)