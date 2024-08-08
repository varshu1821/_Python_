class grandpa():
    def property(self):
        print("grandpa's property")
class dad(grandpa):
    def home(self):
        print("dad's house")
class son(dad):
    def loan(self):
        print("sons loan")
s1 = son()
s1.property()
