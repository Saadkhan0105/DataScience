# Write a program that takes a list of numbers and removes all duplicates using a set.

def remove_duplicates(numbers):
    return list(set(numbers))

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = remove_duplicates(numbers)
print("Original list:", numbers)
print("List after removing duplicates:", unique_numbers)
