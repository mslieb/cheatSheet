class Animal():
    def __init__(self, fur):
        print("Animal created")
        self.fur = fur

    def report(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self,fur):
        Animal.__init__(self,fur)
        print("Dog created")
        #over write report method of Animal
    def report(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog('fuzzy fur')
d.report()
d.eat()
d.bark()
print(d.fur)