class employee():
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
class manager(employee):
     def __init__(self,name,salary,dept):
         super().__init__(name,salary)
         self.dept = dept
     def display(self):
         print("NAME:",self.name)
         print("SALARY:",self.salary)
         print("DEPARTMENT:",self.dept)

emp = manager("Varshu",40000,"IT")
emp.display()
