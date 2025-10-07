# Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")