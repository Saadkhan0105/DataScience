def sum(a, b):
    print("Hey i am summing these numbers")
    c = a + b
    global z # It will use the global variable z instead of creating a new local variable
    z = 0. # this will refer to global variable z and not create a new local variable
    return c

z = 3
print(sum(3, 12))
print(z)