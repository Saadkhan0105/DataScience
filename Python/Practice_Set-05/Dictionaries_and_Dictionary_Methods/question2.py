'''
Create a dictionary of three friends and their phone numbers. Use:

keys() to get all names
values() to get all numbers
items() to loop over key-value pairs and print them
'''
friends = {"Alice": "123-456-7890", "Bob": "987-654-3210", "Charlie": "555-555-5555"}
print(friends.keys())
print(friends.values())
for name, number in friends.items():
    print(f"{name}: {number}")
    