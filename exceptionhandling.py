# exception handling
try:
    a=10
    b=0
    print(a/b)
except:
    print("Error occured")
# this is used when we need to try something that we are not sure
#we have to write except everytime we use try functio


try:
    print("hello")
except:
    print("Meow")
finally:
    print("Finally")

# same finally does same 
#but finally is printed every time 