


class Car:
    # Class attribute
    number_of_wheels = 4

    def __init__(self, model, price):
        self.model = model
        self.price = price

    def start(self):
        print("Car goes broom! broom!")

obj = Car("XYZ", 500000)
obj.start()