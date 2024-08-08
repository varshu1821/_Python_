class teacher:
    def __init__(self, s_name, s_age):
        self.name = s_name
        self.age = s_age
    def display(self):
        print("NAME:", self.name)
        print("AGE:", self.age)

T1 = teacher("Kammu", 24)
T2 = teacher("Dine" , 23)
T1.display()
T2.display()
