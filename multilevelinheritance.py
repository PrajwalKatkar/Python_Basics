class Person:
    def name(self):
        print("This is my name")
        
class Employee(Person):
    def salary(self):
        print("This is my salary")
class Manager(Employee):
    def role(self):
        print("This is my role")

s=Manager()
s.name()
s.salary()
s.role()