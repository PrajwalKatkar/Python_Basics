class Father:
    def skills(self):
        print("Father : cooking")
class Mother:
    def hobby(self):
        print("Mother: Painting,singing")
class Child(Mother,Father):
    def interest(self):
        print("Child: coding,gaming")
s=Child()
s.skills()
s.hobby()
s.interest()