def add(a, b, plus=0):
    x = a + b + plus
    return x

c = add(2, 3, 5)
print(c)  

c1 = add(b=5, a=3, plus=12)
print(c1)