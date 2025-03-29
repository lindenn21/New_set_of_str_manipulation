# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
# Ask user to input something
# Change small letters to capital and capital to small leters
# print

text = input("Enter something: ")
character = []
for i in text:
    if i.isupper():
        character.append(i.lower())
    else:
        character.append(i.upper())
print(character)
