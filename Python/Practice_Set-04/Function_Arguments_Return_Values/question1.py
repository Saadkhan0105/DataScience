# Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".

def full_name(first, last):
    return f"{first} {last}"

name = input("Enter your first name: ")
lname = input("Enter your last name: ")
print(full_name(name, lname))
