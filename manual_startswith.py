# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
# Ask user to input something
# If the string starts with HELLO, print true

text = input("Enter a string, this will check if you start with HELLO: ")
beginning = "HELLO"
if text[:len(beginning)] == beginning:
