# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
# Ask user to input
# If input is lower, print true

text = input("Enter string, this will check if the string you entered is all lower case: ")
if text == text.lower():
    print("True")
else:
    print("False")