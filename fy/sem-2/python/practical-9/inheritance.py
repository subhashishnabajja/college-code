class Base:
    def add(self, a, b):
        print(a + b)

class Derived(Base):
    def subract(self, a, b):
        print(a - b)


obj = Derived()
obj.add(5, 3)
obj.subract(5, 3)
