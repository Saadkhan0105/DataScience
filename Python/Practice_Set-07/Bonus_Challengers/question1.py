# Combine a decorator with *args and **kwargs support so it can wrap any function regardless of its parameters.

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

result = add(2, 3)
print(result)

result = add(a=2, b=3)
print(result)
