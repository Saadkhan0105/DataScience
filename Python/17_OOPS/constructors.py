class Employee:
    
    def __init__(self, salary, name, bond):
        self.salary = salary # create an instance variable of name salary and assign it with salary
        self.name = name
        self.bond = bond
    
    def get_salary(self): 
        return self.salary
    
    def get_info(self):
        return f"The name of the employee is {self.name} and salary is {self.salary}. The bond is {self.bond} years."
    
    
e1 = Employee(34000, "Saad", 4)
print(e1.get_salary())
print(e1.get_info())
