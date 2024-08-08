class person:
    def __init__(self,name):
        self.name = name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade= grade
    def display(self):
        print(self.name)
        print(self.grade)

p1= student("Varshu","A")
p1.display()
