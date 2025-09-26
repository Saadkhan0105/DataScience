# PYTHON

## Variables:
- In python, variables are used to store data that can be used and maipulated thorughout a program.
- A variable is created the moment you assign a value to it using the assignment operator (=).
- Example: 
```
age = 34 # integer
name = "Saad" # string
cgpa = 9.1 # float
```
Here:

	•	age stores an integer.
	•	name is a variable storing a string.
	•	cgpa is storing a floating value

- We don’t need to declare the type explicitly Python is dynamically typed.

Rules of Defining a variable in Python:

	•	Variable names must start with a letter (a-z, A-Z) or an underscore(_).
	•	They can contain letters, numbers, and underscores.
	•	Variable names are case-sensitive (age and Age are different).
	•	Avoid using Python keywords (e.g., if, for, while) as variable names.

## Datatypes:
- Python supports several built-in datatypes:
1. Numeric Types:
   - int: Integer values (e.g., 5, -3, 0)
   - float: Floating-point numbers (e.g., 3.14, -0.001)
   - complex: Complex numbers (e.g., 2 + 3j)
2. Sequence Types:
   - list: Ordered, mutable collection of items (e.g., [1,2, 3])
   - tuple: Ordered, immutable collection of items (e.g., (1,2))
   - range: Represents a sequence of numbers (e.g., range(0, 10))
3. Text Type:
   - str: String of characters (e.g., "Hello, World!")
4. Set Types:
   - set: Unordered collection of unique items (e.g., {1, 2, 3})
   - frozenset: Immutable version of a set (e.g., frozenset({1, 2, 3}))
5. Mapping Type:
   - dict: Collection of key-value pairs (e.g., {"name": "Alice", "age": 28})
6. Boolean Type:
   - bool: Represents True or False values.
7. None Type:
   - NoneType: Represents the absence of a value (e.g., None).
   
## TypeCasting:
- Typecasting is the process of converting one datatype to another.
- In Python, you can use built-in functions to perform typecasting:
1. int(): Converts a value to an integer.
2. float(): Converts a value to a floating-point number.
3. str(): Converts a value to a string.
4. list(): Converts a value to a list.
5. tuple(): Converts a value to a tuple.
6. set(): Converts a value to a set.
7. dict(): Converts a value to a dictionary (if applicable).
- Example:

```
# Convert String to an integer
num_str = "10"
num_int = int(num_str)
print(num_int)  # Output: 10
print(type(num_int))

# Convert String to an integer
num = 25
num_str = str(num)
print(num_str)  # Output: 25
print(type(num_str))

# Convert float to integer
pi = 3.14
pi_int = int(pi)
print(pi_int)  # Output: 3
print(type(pi_int))
```

## Taking User Input 
- In Python, you can take user input using the input() function.
- By default, input() returns a string. We can convert it to other datatypes as needed.
- Example:
```
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} is years old! ")
```

## Comments, Escape Sequences and Print Statements
- Comments are used to explain code and make it more readable. In Python, comments start with the # symbol.
- Example:
```
# This is a single-line comment
print("Hello, World!")  # This prints a message to the console
```
- For multi-line comments, you can use triple quotes (''' or """).
- Multi-line comments are useful for explaining complex code or providing detailed information.
- They can also be used to temporarily disable code during debugging
```
'''
This is a multi-line comment.
It can span multiple lines.
'''
```
- Escape sequences are special characters that are used to represent certain whitespace or control characters within strings. They start with a backslash (\).
- Common escape sequences include:
   -	\n: New line
   -	\t: Tab
   -	\\: Backslash
   -	\": Double quote
   -	\': Single quote
- Example:
```
print("Hello,\nWorld!")  # Output: Hello,
                           #         World!
print("Hello,\tWorld!")  # Output: Hello,    World!
print("He said, \"Hello!\"")  # Output: He said, "Hello
```

## Operators:
- Operators are special symbols that perform operations on variables and values.
- Python supports various types of operators:
1. Arithmetic Operators: +, -, *, /, %, // (floor division), ** (exponentiation)
2. Comparison Operators: ==, !=, >, <, >=, <=
3. Logical Operators: and, or, not
4. Assignment Operators: =, +=, -=, *=, /=, %=, //=
5. Bitwise Operators: &, |, ^, ~, <<, >>
6. Membership Operators: in, not in
7. Identity Operators: is, is not

- Example:
```
a = 10
b = 3
print(a + b)  # Output: 13
print(a > b)  # Output: True
print(a and b)  # Output: 3
a += 5
print(a)  # Output: 15
```

