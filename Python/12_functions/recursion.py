'''
0 1 1 2 3 5 8 13

fib(0) = 0
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
fib(5) = 5
fib(n) = fib(n-2) + fib(n-1) 
'''

def fib(n):
    # Base Case
    if (n == 0 or n == 1):
        return n
    # Recursive Case
    return fib(n-2) + fib(n-1)
print(fib(6))
