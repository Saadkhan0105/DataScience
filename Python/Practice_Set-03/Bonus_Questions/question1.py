# Write a program that counts how many vowels are in a given string.

sentence = input("Enter a string: ")
count = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for char in sentence:
    if(char in vowels):
        count += 1
print(f"Total number of vowels in the given string is: {count}")
