class Employee:
    company = "ASUS" # class variable
    
    def __init__(self, salary, name, bond, company):
        self.salary = salary # create an instance variable of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company
    
    def get_salary(self): 
        return self.salary
    
    def get_info(self):
        return f"The name of the employee is {self.name} and salary is {self.salary}. The bond is {self.bond} years."
    
e1 = Employee(34000, "Saad", 4, "Tesla")
print(e1.company) # accessing class variable
print(Employee.company) # accessing class variable using class name

# Object Introspection:
print(dir(e1)) # dir() function gives all the attributes and methods of an object