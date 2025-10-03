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

- Strings are immutable, meaning once a string is created, it cannot be changed or modified.
- Example:
```
name = "Saad"
name[0] = "P"  # This will raise an error
```

### String Methods:
- Python provides several built-in string methods that allow you to manipulate and work with strings.
- Some commonly used string methods include:
1. lower(): Converts all characters in the string to lowercase.
2. upper(): Converts all characters in the string to uppercase.
3. strip(): Removes leading and trailing whitespace from the string.
4. replace(old, new): Replaces occurrences of a substring with another substring.
5. split(separator): Splits the string into a list of substrings based on the specified separator.
6. join(iterable): Joins elements of an iterable (like a list) into a single string, with the string as the separator.
- Example:
```
name = "  Saad Khan  "
print(name.lower())  # Output: saad khan
print(name.upper())  # Output: SAAD KHAN
print(name.strip())  # Output: Saad Khan
print(name.replace("Saad", "Ali"))  # Output:   Ali Khan
print(name.split())  # Output: ['Saad', 'Khan']
words = ["Hello", "World"]
print(" ".join(words))  # Output: Hello World
```

### String Formatting:
- String formatting allows you to create strings with dynamic content by embedding variables or expressions within a string.
- Python provides several ways to format strings:
1. f-strings (formatted string literals): Introduced in Python 3.6,
    - Example:
    ```
    name = "Saad"
    age = 34
    print(f"My name is {name} and I am {age} years old.")
    ```
2. str.format() method:
    - Example:
    ```
    name = "Saad"
    age = 34
    print("My name is {} and I am {} years old.".format(name, age))
    ```
3. %-formatting (old-style formatting):
    - Example:
    ```
    name = "Saad"
    age = 34
    print("My name is %s and I am %d years old." % (name, age))
    ```

## Functions:
### Defining Functions in Python:
- Functions are reusable blocks of code that perform a specific task.
- They help in organizing code, improving readability, and reducing redundancy.
- In Python, functions are defined using the def keyword, followed by the function name and parentheses
- Example:
```
def greet(name):
    return f"Hello, {name}!"
print(greet("Saad"))  # Output: Hello, Saad!
``` 
### Key Points:
- Define using def keyword.
- Function name should be descriptive.
- Use `return` to send a value back

### Functions Arguments and Return Values:
- Functions can accept inputs called arguments or parameters.
- There are different types of function arguments:
1. Positional Arguments: Arguments are passed in the same order as the parameters are defined.
    - Example:
    ```
    def add(a, b):
         return a + b
    print(add(2, 3))  # Output: 5
    ```
2. Keyword Arguments: Arguments are passed by explicitly specifying the parameter name.
    - Example:
    ```
    def add(a, b):
         return a + b
    print(add(b=3, a=2))  # Output: 5
    ```
3. Default Arguments: Parameters can have default values, which are used if no argument is provided
    - Example:
    ```
    def greet(name="Guest"):
         return f"Hello, {name}!"
    print(greet())  # Output: Hello, Guest!
    print(greet("Saad"))  # Output: Hello, Saad!
    ```

### Lambda Functions:
- Lambda functions are small anonymous functions defined using the lambda keyword.
- They can take any number of arguments but can only have a single expression.
- Example:
```
square = lambda x: x * x
print(square(5))
```

### Recursion:
- Recursion is a programming technique where a function calls itself to solve a problem.
- A recursive function typically has a base case to stop the recursion and a recursive case to continue.
- Example:
```
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case
print(factorial(5))  # Output: 120
```

## Modules and Pip (using external libraries):

There are two type of modules in Python:
1. Built-in Modules: These are pre-installed with Python and can be used directly without any
   additional installation. Examples include `math`, `sys`, `os`, etc.
2. External Modules: These are third-party modules that need to be installed separately using package
   managers like pip. Examples include `numpy`, `pandas`, `requests`, etc.
### Key Points:
- Modules are files containing Python code that can define functions, classes, and variables.
- They allow you to organize your code into separate files and reuse code across different programs.
- You can create your own modules or use built-in modules and third-party libraries.
- To use a module, you can import it using the import statement.
- Example:
```
import math
print(math.sqrt(16))  # Output: 4.0
```
- Pip is the package installer for Python. It allows you to install and manage third-party libraries and packages.
- To install a package using pip, you can use the command:
```
pip install requests

import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Output: 200
```

## Function Scope:
- Scope refers to the visibility and accessibility of variables and functions in different parts of a program.
- In Python, there are two main types of scope:
1. Local Scope: Variables defined within a function are in the local scope and can only be
    accessed within that function.
2. Global Scope: Variables defined outside of any function are in the global scope and can be
    accessed from anywhere in the program.
- Example:
```
def my_function():
    local_var = "I am local"
    print(local_var)  # Accessible here
my_function()
# print(local_var)  # This will raise an error
global_var = "I am global"
print(global_var)  # Accessible here
def another_function():
    print(global_var)  # Accessible here
another_function()
```

## Docstrings:
- Docstrings are special strings used to document functions, classes, and modules in Python.
- They provide a way to describe the purpose, parameters, and return values of a function or
    class.
- Docstrings are defined using triple quotes (''' or """) and are placed immediately after the
    function or class definition.
- Example:
```
def greet(name):
    """
    This function greets the person with the given name.
    
    Parameters:
    name (str): The name of the person to greet.
    
    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"
print(greet("Saad"))  # Output: Hello, Saad!
```