'''
Write a function print_details(**kwargs) that prints key-value pairs passed as arguments, for example:
   print_details(name="Alice", age=25, city="Delhi")
   # Output:
   # name: Alice
   # age: 25
   # city: Delhi
'''

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="Delhi")