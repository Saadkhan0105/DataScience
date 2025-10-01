# Take a user input string and check if it is a palindrome (same forwards and backwards).

user_input = input("Enter a string: ")

if(user_input == user_input[::-1]):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")