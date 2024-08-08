class a():
    def __init__(self):
        print("you are in class A")
    def display(self):
        print("audio")
class b(a):
    def __init__(self):
        super().__init__()
        print("you are in class B") 
    def display(self):
        print("disk")
class c(b,a):
    def __init__(self):
         super().__init__()
         print("you are in class C")
    def display(self):
        print("video")

c1=c()















