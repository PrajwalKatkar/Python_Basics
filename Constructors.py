class Employee:
    name = "Harry" #this are class attributes 
    language = "Java"
    salary = 1200000  

    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary
        

harry = Employee("prajwal", "javascript",12000)
print(harry.name,harry.language,harry.salary)  
harry = Employee("rashid", "python",12000)
print(harry.name,harry.language,harry.salary)  

harry.age = 20 #this is instance attribute