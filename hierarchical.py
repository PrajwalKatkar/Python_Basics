class Parent:
    def name(self):
        print("This is my name")
        
class Child1(Parent):
    def salary(self):
        print("This is my salary")
class Child2(Parent):
    def role(self):
        print("This is my role")

s1=Child1()
s2=Child2()
s1.name()
s2.name()
s1.salary()
s2.role()
