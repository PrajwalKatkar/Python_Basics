# single inheritance
class A:
    a=10
class B(A):
    def display(self):
        print(self.a)
h=B()
h.display()