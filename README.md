# Variables:
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

# Datatypes:
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
   
# TypeCasting:
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
