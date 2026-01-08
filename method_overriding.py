# in methods overriding = methods name are same and parameters are also same 

class Parent:
    def show(self):
        print("This is parent class method")
class Child(Parent):
    def show(self):
        super().show()
        
        print("This is child class method")
c=Child()
c.show()

        