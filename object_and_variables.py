class bangalore:
    water = "yes"
    def intern(self):
        print("work")
    def visit(self):
        print("Mall")
virat = bangalore()
kohli = bangalore()
virat.intern()
kohli.visit()
virat.water = "No"
print(virat.water)
kohli.water= "maybe"
print(kohli.water)
