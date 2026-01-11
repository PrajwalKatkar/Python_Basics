#functions of list 
hello = ["Prajwal", "Rishabh", 17 , 54.2,"india","canada"]

hello.append("Salman") # it will add the string in the end
print(hello)


#sort 

l1 = [25 , 26 ,2,1,58,98,42]
l1.sort()
print(l1)

#reverse 
l2 = [25 , 26 ,2,1,58,98,42]
l2.reverse()
print(l2)


# to insert in middle we have to use insert function

l2.insert(3,2222) #it will add 2222 at index 3 


print(l2)



#to delete something from list we use pop

l2.pop(4)
print(l2)


l2.remove(58)
print(l2)