'''
while True:
    try:
        a = int(input("Enter number 1:"))
        b = int(input("Enter number 2:"))

        print("The division is:", a / b)
    except ValueError:
        print("Invalid input, please enter numeric values.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    except Exception as e:
        print("Invalid input, please try again.", e)
'''
a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))

if b == 0:
    raise ValueError("Please don't divide by 0.")
print(f"The division is: {a / b}")
