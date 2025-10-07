def sum(a, b):
    # a and b are local variables
    c = a + b
    z = 1 # It creates a new local variable z which is destroyed after function ends
    return c

def greet():
    z = 32 # Local variable
    print("Hello")
    
    
z = 8 # Global variable
print(z)  
print(sum(4, 6))
print(z)  