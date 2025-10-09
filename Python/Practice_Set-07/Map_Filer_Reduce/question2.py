# Use filter() to get only even numbers from [10, 11, 12, 13, 14].

numbers = [10, 11, 12, 13, 14]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))