print("--------------------------------HI--------------------------------------")
print("---------------------------STATE BANK OF INDIA-------------------------------")


userList={"varshu":1234,"kammu":2468}
def validate(userid,password,userList):
    if userid not in userList:
        print("user Id does not exists")
        return False
    if userList[userid]!=password:
        print(userList[userid])
        print("incorrect password!!!")
        return False
    return True

user_id=input("enter ur userId:")
password=int(input("enter your password:"))
validate=validate(user_id,password,userList)


class atm:
    def __init__(self,name):
        self.name=name
        self.balance=0
        self.transaction=[]
    def display(self):
        print("-------------Current Balance is:",self.balance,"-------------")
    def deposit(self,amount):
        self.balance+=amount
        print("----------------------Amount depositted successfully!----------------------")
        self.transaction.insert(0,[self.name,"deposited",amount,"Balance",self.balance])
    def withdraw(self,amount):
        if self.balance<amount:
            print("-------------------------insufficient Balance-------------------------")
        else:
            self.balance-=amount
            self.transaction.insert(0,[self.name,"withdraw",amount,"Balance",self.balance])
            print("-------------Current Balance is:",self.balance,"-------------")
            print("-------------------------Collect your Cash-------------------------")
    def Transfer(self,amount):
        if self.balance<amount:
            print("-------------------------insufficient Balance-------------------------")
        else:
            self.balance-=amount
            self.transaction.insert(0,[self.name,"withdraw",amount,"Balance",self.balance])
    def Transhistory(self):
        if len(self.transaction)==0:
            print(" 12/11/2023 (Withdraw) 5000"
                  " 14/11/23  (Deposit) 2000")
        else:
            print("--------------------------- Transaction History---------------------------")
            
            for i in range(len(self.transaction)):
                if self.transaction[i][1]=="deposited":
                    deposit="   "+str(self.transaction[i][2])+"   "
                    withdraw="          "
                elif self.transaction[i][1]=="withdraw":
                    deposit="          "
                    withdraw="   "+str(self.transaction[i][2])+"   "
                print("|","  "+str(self.transaction[i][0])+"  ","|",deposit,"|",withdraw,"|","  "+str(self.transaction[i][4])+"   ","|")
            print("+------------+------------+------------+-----------+")
name=user_id
user_id=atm(name)

while(validate):
    print("1.Transactions History")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.Transfer")
    print("5.Quit")

    choice=int(input("enter your choice:"))
    if choice==1:
        user_id.Transhistory()
    elif choice==2:
        amount=int(input("enter the amount to withdraw:"))
        user_id.withdraw(amount)
    elif choice==3:
        deposit=int(input("enter the amount to Deposit:"))
        user_id.deposit(deposit)
    elif choice==4:
        recipient=input("enter receipient's user ID:")
        transfer=int(input("enter the amount to transfer:"))
        if recipient not in userList:
            print("recipient not found")
            continue
        user_id.Transfer(transfer)
        user_id.display()
    else :
        print("Thankyou, please visit again!!")
        break

    
        
