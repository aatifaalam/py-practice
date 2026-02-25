class Car:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def show(self):
        print(self.name, self.model)

    def isGood(self):

        if self.model <= 2020:
            print("Car is in good condition.")
        else:
            print("Too old car.")        


c1 = Car("BMW", 2020)
c2 = Car("Audi", 2019)

c1.isGood()
c2.isGood()