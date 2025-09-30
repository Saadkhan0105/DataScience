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

## Conditional:
- Conditional statements are used to perform different actions based on different conditions.
- The primary conditional statements in Python are if, elif, and else.
1. if-elif-else:
- The if statement is used to test a specific condition. If the condition is true, the block of code inside the if statement is executed.
- The elif (else if) statement is used to test multiple conditions. If the first condition is false, the program checks the next condition.
- The else statement is used to execute a block of code when all previous conditions are false.
- Example:
```
age = int(input("Enter your age: "))

if (age > 18):
    print("You can drive.")  
elif age == 18:
    print("We will check your documents.") 
else:
    print("Sorry you cannot drive.")
    
print("End of Program.")
```

 2. match:
- The match statement is used for pattern matching, introduced in Python 3.10.
- It allows you to match a value against a series of patterns and execute code based on the matched pattern.
- Example:
```
a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You won a Charger🔌 !")
    case 3:
        print("You won $3")
    case 6:
        print("You won a MacBook💻 !")
    case _:
        print("Bettr luck next time")
```

## Loops:
1. For Loop:
- The for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
- It allows you to execute a block of code multiple times, once for each item in the sequence.
- Example:
```
for i in range(1, 11): 
    print("5 *", i, "=", 5*i)
```

2. While Loop:
- The while loop is used to execute a block of code as long as a specified condition is true.
- It is useful when the number of iterations is not known beforehand and depends on a condition.
- Example:
```
i = 1
while i <= 10:
    print("5 *", i, "=", 5*i)
    i = i + 1
```

3. Break:
- The break statement is used to exit a loop prematurely when a certain condition is met.
- It can be used in both for and while loops.
- Example:
```
for i in range(0, 21):
    print(i)
    if i == 11:
        print("Breaking the loop")
        break
```

4. Continue: 
- The continue statement is used to skip the current iteration of a loop and move to the next iteration.
- It can be used in both for and while loops.
- Example:
```
for i in range(1, 20):
    if i == 10:
        continue
    print(i)
```

5. Pass:
- The pass statement is a null operation; it does nothing when executed.
- It is used as a placeholder in situations where a statement is syntactically required but no action is needed.
- Example:
```
i = 3
if i == 12:
    print("This is a pass statement")
    pass
print("End of the program")
```

## Strings:
- Strings are sequences of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
- Strings are immutable, meaning they cannot be changed after they are created.
- Example:
```
# name = "Saad"
name = 'Saad'
# name = '''Saad'''
print(name)  
```
- Indexing and Slicing:
- Strings can be indexed and sliced to access specific characters or substrings.
- Indexing starts at 0 for the first character, 1 for the second character, and so on. Negative indexing starts from -1 for the last character, -2 for the second last, and so on.
- Example:
```
name = "Saad"
print(name[0])  # Output: S
print(name[1])  # Output: a
print(name[2])  # Output: a
print(name[3])  # Output: d
```
- Slicing allows you to extract a substring by specifying a start and end index.
- Example:
```
name = "Saad"
print(name[0:2])  # Output: Sa (from index 0 to index 2, excluding index 2)
print(name[:3])   # Output: Saa (from start to index 3, excluding index 3)
print(name[1:])   # Output: aad (from index 1 to the end)
print(name[-1])   # Output: d (last character)
print(name[-3:-1]) # Output: aa (from index -3 to index -1, excluding index -1)
```
