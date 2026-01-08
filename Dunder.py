# Dunder method
# string method prints object
# class Bankaccount:
#     def __init__(self,name,balance):
#         self.name=name 
#         self.balance=balance
#     def __str__(self):
#         return self.name + str(self.balance)
# s1=Bankaccount("Prajwal",100000)
# print(s1)

# __len__ method
# class Mydata:
#     def __init__(self,data):
#         self.data=data
#     def __len__(self):
#         return len(self.data)
# d=Mydata([1,2,3])
# print(len(d))

# __add__ method
# class Number:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,n2):
#         return self.x+n2.x
# n1=Number(10)
# n2=Number(20)
# print(n1+n2)

# __sub__
# class Number:
#     def __init__(self,x):
#         self.x=x
#     def __sub__(self,n2):
#         return self.x - n2.x
# n1=Number(10)
# n2=Number(20)
# print(n1-n2)

# __truediv__
# class Number:
#     def __init__(self,x):
#         self.x=x
#     def __truediv__(self,n2):
#         return self.x / n2.x
# n1=Number(10)
# n2=Number(20)
# print(n1/n2)

# __mul__
# class Number:
#     def __init__(self,x):
#         self.x=x
#     def __mul__(self,n2):
#         return self.x * n2.x
# n1=Number(10)
# n2=Number(20)
# print(n1*n2)

# __eq__
# class Number:
#     def __init__(self,x):
#         self.x=x
#     def __eq__(self,n2):
#         return self.x == n2.x
# n1=Number(10)
# n2=Number(20)
# print(n1==n2)

# class Number:
#     def __init__(self,x):
#         self.x=x
#     def __lt__(self,n2):
#         return self.x < n2.x
# n1=Number(10)
# n2=Number(20)
# print(n1<n2)