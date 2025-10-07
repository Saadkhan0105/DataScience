class Employee:
    company = "Google"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return f"The name of the employee is {self.name} and the salary is {self.salary}"
    
    def __repr__(self):
        return f"Employee: {self.name}\nsalary: {self.salary}"
    
    def __len__(self):
        return len(self.name)
        
e = Employee("Saad", 100000)
print(len(e))
print(e.name, e.salary)
print(str(e))
print(repr(e))