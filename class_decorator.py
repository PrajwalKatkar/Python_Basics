# class Employee:
#     a= 1
#     def show(self):
#         print(f"This is Employee class {self.a}")
    
# e= Employee()
# e.a=45
# e.show()
# this is printing the instance variable value 45 instead of class variable value 1
# to overcome this we will use @classmethod decorator

class Employee:
    a= 1
    @classmethod
    def show(cls):
        print(f"This is Employee class {cls.a}")

e= Employee()
e.a=45      
e.show()
# this is printing the class variable value 1 because we used @classmethod decorator
