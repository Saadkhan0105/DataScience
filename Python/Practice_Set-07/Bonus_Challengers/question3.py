# Create a small program where invalid user input raises a custom exception, logs the error, and continues execution instead of crashing.

import logging

# Configure logging to write errors to a file
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Custom exception
class InvalidInputError(Exception):
    """Raised when the user enters invalid input."""
    pass

def get_number():
    user_input = input("Enter a positive number: ")
    if not user_input.isdigit() or int(user_input) <= 0:
        raise InvalidInputError(f"Invalid input: '{user_input}' is not a positive number.")
    return int(user_input)

# Main loop — program continues even if input is invalid
while True:
    try:
        number = get_number()
        print(f"✅ You entered: {number}")
        break  # Exit loop on valid input
    except InvalidInputError as e:
        print(f"❌ Error: {e}. Please try again.")
        logging.error(e)