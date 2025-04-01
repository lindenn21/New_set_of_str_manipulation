# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
# Ask user to input
# Count how many times the same thing appears

total_count = 0
list_word = []
for i in range(5):
    text = input(f"Enter string {i + 1}: ")
    list_word.append(text)

count_string = input("Input the word that you entered and would like to count how many times it appeared: ")

for text in list_word:
    count = 0
    strings = text.split()
    for list_word in strings:
        if list_word == count_string:
            count += 1

print(total_count)



