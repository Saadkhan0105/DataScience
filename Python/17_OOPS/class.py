class Employee:
    company = "HP"
    
    def get_salary(self):
        print(self)
        return 34000
    
e = Employee() # An objecrt of class Employee is created here
print(e.get_salary()) # The method get_salary is called using the object e
print(e.company)

e2 = Employee()
print(e2.get_salary())
print(e2.company)