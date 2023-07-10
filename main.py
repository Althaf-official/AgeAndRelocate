class MasGroupAndCompanies():

    year=2023#global variable

    def __int__(self,name,age,place):#constructor
        self.Name=name
        self.Age=age
        self.Place=place

    def add_age(self):
        self.Age=self.Age+1

    def relocate(self,place):
        self.Place=place

    def display(self):
        print(f"age is : {self.Age}  and place is :{self.Place}")

