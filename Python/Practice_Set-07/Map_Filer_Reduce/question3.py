# Use reduce() from functools to find the product of all elements in [1, 2, 3, 4].

import functools

list1 = [1, 2, 3, 4]

print(functools.reduce(lambda x, y: x*y, list1))