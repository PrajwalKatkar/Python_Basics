class Employee:
    name = "Harry" #this are class attributes 
    language = "Java"
    salary = 1200000  
    def funny(self):
     print(f"The name of the Employee is {self.name} and his salary is {self.salary}")


harry = Employee()
harry.age = 20 #this is instance attribute
harry.funny()