class Parent:
    def name(self):
        print("This is my name")
        
class Child1(Parent):
    def role(self):
        print("This is my role")

class Child2(Parent):
    def role1(self):
        print("This is my role")

class Parent2(Child1,Child2):
    def salary(self):
        print("This is my salary")
s1=Parent2()
s1.name()
s1.role()
s1.role1()
s1.salary()