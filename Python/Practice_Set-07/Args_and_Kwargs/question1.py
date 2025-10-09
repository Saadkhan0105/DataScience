# Write a function sum_all(*args) that accepts any number of integers and returns their sum.

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))