marks = {"Saad": 54, "Abuzar": 45, "Umaimah": 93}

print(marks.keys())  # Prints all the keys in the dictionary
print(marks.values())  # Prints all the values in the dictionary
print(marks.items())  # Prints all the key-value pairs in the dictionary
marks.update({"Saad": 100, "Ali": 67})  # Updates the dictionary with new key-value pairs
print(marks)
marks.pop("Ali")  # Removes the key-value pair with the specified key
print(marks)
marks.popitem()  # Removes the last key-value pair from the dictionary
print(marks)
marks.clear()  # Clears the dictionary
print(marks)