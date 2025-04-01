# Ask user to input something
# Capitalize the first letter of every word
# Print

text = input("Enter:")
list_word = text.split()
capitalize = [word.capitalize() for word in list_word]
title = ''.join(capitalize)
print(title)
