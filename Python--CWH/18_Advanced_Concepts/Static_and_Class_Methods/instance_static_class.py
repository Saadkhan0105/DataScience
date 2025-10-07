class Employee:
    company = "Google"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    # Instance Method
    def print_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")
        
    # Static Method
    @staticmethod
    def sum(a, b):
        return a + b
    
    # Class Method
    @classmethod
    def print_company(cls):
        print(cls.company) 
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Saad", 100000)
e2 = Employee("Abuzar", 120000)
# print(Employee.company)
# print(Employee.name)

e1.print_info()
e2.print_info()

# print(e2.sum(5, 7))
print(Employee.company)
e1.change_company("Amazon")
print(Employee.company)
