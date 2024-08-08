class dad():
    def laptop(self):
        print("dads laptop")
class mom():
    def oven(self):
        print("mom's oven")
class son(dad, mom):
    def pizza(self):
        print("my pizza!!!!")
s1 = son()
s1.oven()
