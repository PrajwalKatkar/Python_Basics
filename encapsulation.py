class Student:
    def __init__(self,marks,name):
        self.marks=marks
        self.name=name
    def show(self):
        print(f"Name {self.name} Marks {self.marks}")
    
s=Student("Prajwal",100)
s.show()