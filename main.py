class Person:
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place=place

    def add_age(self):
        self.age=self.age+1

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old. and my place is {self.place}")

    def relocate(self,place):
        self.place=place

# Creating an instance of the Person class with arguments
person1 = Person("Muhammed althaf", 27, "kallambalam")
person1.introduce()  # Output: My name is Alice and I am 25 years old.

person2 = Person("jaseela ashraf ", 21, "idavoorkonam")
person2.relocate("madanthapacha")
person2.add_age()
person2.introduce()  # Output: My name is Bob and I am 30 years old.





