class Animal:
    def __init__(self):
        self.name = "Nameless"
    def setName(self, newName):
        self.name = newName

class Cat(Animal):
    def __init__(self):
        pass
    def test(self):
        print(self.name)

cat1 = Cat()
cat1.test()