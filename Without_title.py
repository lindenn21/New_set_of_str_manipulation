# Ask user to input something
# Lower the whole string
# Upper the first letter
# Print

text = input("Enter:")
capitalize = text[:1].upper() + text[1:].lower()
print(capitalize)