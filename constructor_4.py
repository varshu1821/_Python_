class fruit:
    def __init__(self,f_color):
        self.color = f_color
    def display(self):
        print(" FRUIT COLOR:", self.color)

apple = fruit("RED")
apple.display()
