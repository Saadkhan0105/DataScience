class Animal:
    location = "forest" # class variable
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Generic animal sound")
        
class Dog(Animal): # Dog class inherits from Animal class
    def speak(self): # overriding the speak method
        super.speak() # calling the parent class method
        print(f"{self.name} says Woof Woof!")

class Cat(Animal): # Cat class inherits from Animal class
    def speak(self): # overriding the speak method
        print(f"{self.name} says Meow Meow!")
        
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

print(my_dog.name) # accessing instance variable from parent class
my_dog.speak() # calling overridden method
print(my_dog.location) # accessing class variable from parent class

print(my_cat.name) # accessing instance variable from parent class
my_cat.speak() # calling overridden method
print(my_cat.location) # accessing class variable from parent class