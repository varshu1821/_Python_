namelist = ["john","jay","tom","harry","sally","lilly","ray","jose","jas","rose"]
date=input("Enter the attendance date (DD-MM-YYYY):")
print("ATTENDANCE FOR :",date)
print("=========================================================================")
class attendance_sys:
    def __init__(self,date):
        self.date= date
        self.dic={"5-08-2024":{" john ":"P"," jay ":"P"," tom ":"A"," harry":"P","sally ":"A"," lilly ":"P"," ray":"A"," jose ":"A","  jas ":"P","rose":"A"}}
    def attendance(self,date,namelist):
        initial=100
        self.dic[date]= {}
        for i in range(len(namelist)):
            initial+=1
            template=namelist[i]+"(Roll No:"+str(initial)+")"+"(enter P or A):      "
            self.dic[date][namelist[i]]=input(template)
    def display(self,date,namelist):
        prev = list(self.dic.keys())
        print("\n=========================ATTENDANCE HISTORY==========================\n")
        header = ""
        print("+-----------+------------+------------+")
        print("|    NAME   |",prev[0],"|",prev[1],"|")
        print("+-----------+------------+------------+")
        for i in range(len(namelist)):
            template="|"+namelist[i]+"|"+self.dic[prev[0]][namelist[i]]+"|"+self.dic[prev[1]][namelist[i]]+"|"
            print(template)
            print("+-----------+------------+------------+")
        print(self.dic)

        
day=attendance_sys(date)
day.attendance(date,namelist)
day.display(date,namelist)

        
    
