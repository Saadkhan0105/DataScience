# Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.

import my_utils

def is_even(n):
    return my_utils.is_even(n)

# Example usage:
print(is_even(4))  
print(is_even(5))  