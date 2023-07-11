class Person:
    year=2023
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place=place

    def add_age(self):
        self.age=self.age+1

    def relocate(self,place):
        self.place=place

    def display(self):
        print(f"The year is {str(Person.year)} and My name is {self.name} and I am {self.age} years old. and my place is {self.place}")

    #class method function
    """
classmethod decorator is used to define a class method. 
A class method is a method that belongs to the class itself rather than an instance of the class. 
It can be called on the class directly, without the need to create an instance of the class.
To define a class method, you need to decorate a method within the class using the @classmethod decorator. 
The method should have a special first parameter conventionally named cls, which refers to the class itself. 
This parameter allows you to access and modify class-level variables and call other class methods.
    """
    @classmethod
    def add_year(cls):
        cls.year=cls.year+1

    @staticmethod
    def display_welcome():
        print("--------------------Welcome to Mas Group and Comapanies---------------------------")

Person.display_welcome()

# Creating an instance of the Person class with arguments
person1 = Person("Muhammed althaf", 27, "kallambalam")
person2 = Person("jaseela ashraf ", 21, "idavoorkonam")

person1.display()
person2.display()

print("________________________________________________")

Person.year=Person.year+1
person1.add_age()
person2.add_age()

person1.display()
person2.display()

print("________________________________________________")
Person.add_year()
#person1.add_age()
#person2.add_age()
person1.relocate("Abu Dhabi")
person2.relocate("madanthapacha")

person1.display()
person2.display()

print("________________________________________________")




