'''
s = "hello world"

s[0] = "P"

a = len(s)
print(a)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
 
text = " hello world "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

text1 = "Python is fun"
print(text1.find("is"))
print(text1.replace("fun", "great"))

text2 = "Apples, Bananas, Pineapples"
print(text2.split(","))
print(",".join(["Apples", "Bananas", "Pineapples"]))
'''
text3 = "Python123"
print(text3.isalnum())
print(text3.isalpha())
print(text3.isdigit())
print(text3.islower())
print(text3.isupper())