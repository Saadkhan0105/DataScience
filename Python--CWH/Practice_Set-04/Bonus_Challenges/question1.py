# Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
def fibonacci(n, a=0, b=1):
    if n <= 0:
        return
    print(a, end=' ')
    fibonacci(n-1, b, a+b)
fibonacci(10)  
