class Employee:
    name = "Harry" #this are class attributes 
    language = "Java"
    salary = 1200000  

harry = Employee()
harry.language = "React" #this is instance attribute  and its priority is more than class atribute


print(harry.name , harry.language,harry.salary)    