# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
# Ask user to input something
# Specify the amount of spaces needed
# Center it based on the amount
# Print

text = input("Enter: ")
center1 = int(input("The number of spaces: "))

center_to = center1 + len(text)
center_to2 = center1 + -len(text)
space = " " * center_to
space2 = " " * center_to2

print(f"/{space}{text}{space2}/")