# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.
# Ask user to input
# Add space at the beginning
# print

text = input("Enter your name: ")
spaces = int(input("Enter the amount of spaces you desire:"))
manual_rjust = " " * spaces + text
print(manual_rjust)

