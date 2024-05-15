class Cake:
    def __init__(self, kind, price, slices):
        self.kind = kind
        self.price = price
        self.slices_remaining = slices
    
    def describe(self):
        return f"This is a {self.kind} cake. It costs ${self.price} and has {self.slices_remaining} slices remaining."

    def sell(self, count):
        if count <= 0:
            return "Can't sell zero or negative slices."
        elif self.slices_remaining - count < 0:
            return "Can't sell more slices than we have."
        else:
            self.slices_remaining -= count
            return f"{count} slices sold. {self.slices_remaining} slices remaining."


# Creating instances of the Cake class
spice_cake = Cake("Spice Cake", 15, 8)
chocolate_cake = Cake("Chocolate Cake", 20, 6)

# Selling slices of cakes
print(spice_cake.describe())
print(spice_cake.sell(5))  # Sell 5 slices
print(spice_cake.sell(4))  # Try to sell 4 more slices
print(chocolate_cake.describe())
print(chocolate_cake.sell(0))  # Try to sell 0 slices
print(chocolate_cake.sell(-1))  # Try to sell -1 slices
