'''
Write a program using match case that simulates a simple calculator.

Ask the user for two numbers and an operation (+, -, *, /).
Perform the operation using match case.
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")

match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2
    case _:
        print("Invalid operator")
        exit()

print("The result is:", result)