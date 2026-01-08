# same method name, but different behaviour
class animal:
    def sound(self):
        print("Animals makes sound")
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
d=[animal(),Dog(),Cat()]
for a in d:
    a.sound()