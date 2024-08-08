class phone:
    charger_type = "c-type"
    def __init__(self, Brand,Price):
        self.brand = Brand
        self.price = Price

    def display(self):
        print("BRAND :" , self.brand)
        print("PRICE :" , self.price)
        print("CHARGER TYPE:" , self.charger_type)

sam = phone("Samsung", 90000)
one = phone("Oneplus", 70000)
pixel = phone("google", 80000)
sam.display()
one.display()
pixel.display()
