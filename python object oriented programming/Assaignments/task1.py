class Cake:
    def __init__(self, kind, price, slices):
        self.kind = kind
        self.price = price
        self.slices = slices
    
    def describe(self):
        return f"This is a {self.kind} cake. It costs ${self.price} and has {self.slices} slices."


# Creating instances of the Cake class
spice_cake = Cake("Spice Cake", 15, 8)
chocolate_cake = Cake("Chocolate Cake", 20, 10)

# Checking if the describe method works for each instance
print(spice_cake.describe())
print(chocolate_cake.describe())