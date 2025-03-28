# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
# Ask user to input whatever
# Ask user how far the space should be
# print

text = input("Input anything: ")
how_far = int(input("Enter how far the space will go: "))

space = how_far - len(text)
