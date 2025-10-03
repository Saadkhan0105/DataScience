# Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.
def multiply(a, b):
    """
    Multiplies two numbers a and b and returns the result.
    
    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.
    
    Returns:
    int, float: The product of a and b.
    """
    return a * b

print(multiply(5, 3))  
print(multiply(2.5, 4))  
help(multiply)