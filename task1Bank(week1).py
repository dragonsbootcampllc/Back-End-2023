class Bank():
    def __init__(self,name,id,accountNumber) :
        self.name=name
        self.id=id
        self.accountNumber=accountNumber
        self.balance=0
        self.deposits=0
        self.withdraws=0
        self.transfers=0

    def deposit(self,d):
            self.d=d
            self.balance+=d
            self.deposits+=1
            print(f"The money has been deposited successfully\nYour new balance is {self.balance}")
            

    def withdraw(self,w):
                self.w=w
                if w>self.balance:
                    print(f"Sorry,You cant withdraw this money beacuse your balance is {self.balance}")
                else:
                    self.balance-=w
                    self.withdraws+=1
                    print(f"The money has been withdrawn successfully\nThe new balance is {self.balance}")

    def transfer(self,t):
         self.t=t
         if t>self.balance:
                    print(f"Sorry,You cant transfer this money beacuse your balance is {self.balance}")
         else:
                    self.balance-=t
                    self.transfers+=1
                    print(f"The money has been transfered from this account successfully\nThe new balance is {self.balance}")
    
    def details(self):
                 print(f"Hello,MR.{self.name}\nYour ID is {self.id}\nYour balance is {self.balance} ")

    def transactions(self):
                 print(f"The number of deposits {self.deposits}\nThe number of withdraws {self.withdraws}\nThe number of transfers between accounts is {self.transfers}  ")             




print("Welcome to The bank System\nFirst,Please Create an account to enjoy our services")
name=input("Please,Enter Your name\n")
id=int(input("Please,Enter Your ID\n"))
b1=Bank(name,id,2003)
while True:
     o=int(input("#######################################################################################################\nEnter the option number you want\nTo create another account press 1\nTo deposit press 2\nTo withdraw press 3\nTo transfer between accounts press 4\nTo show details of the account press 5\nTo show all transactions press 6\nTo Quit press 7\n"))
     if o==7:
          break
     elif o==1:
          b2=Bank(name,id,2004)
          print("Account created successfully\n")
     elif o==2:
       d=int(input("Please,Enter the amount you want to deposit\n"))
       b1.deposit(d)
     elif o==3:
          w=int(input("Please,Enter the amount you want to withdraw\n"))
          b1.withdraw(w)
     elif o==4:
           t=int(input("Please,Enter the amount you want to transfer to another account\n"))
           b1.transfer(t)    
     elif o==5:
        b1.details()
     elif o==6:
         b1.transactions()   
