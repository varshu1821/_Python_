class laptop:
    def __init__(self):
        self.price = 30000
        self.processor = "i5"
    def display(self):
        print("PRICE", self.price)
        print("PROCESSOR", self.processor)
hp=laptop()
hp.price = 50000
hp.processor = "i7"
hp.display()
