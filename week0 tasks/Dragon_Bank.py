
# ? Task 1:Bank system:
#   * Create a class for the bank system that represents
#   * the different objects in the system (customers, accounts, transactions).
#   * Create methods for the bank system that create, deposit, withdraw,
#   * and transfer money between accounts.
#   * Create a main method that allows the user to interact with the bank system.

class Bank():
  def __init__(self,name,id,accountnumber) :
    self.name=name
    self.id=id
    self.accountnumber=accountnumber
    self.balance=0
    self.deposits=0
    self.withdraws=0
    self.transfers=0

  def deposit(self,deposit):
      self.deposit=deposit
      self.balance+=deposit
      self.deposits+=1
      print(f"The money has been deposited successfully\n")
      print(f"Your new balance is {self.balance}")

  def withdraw(self,withdraw):
    self.withdraw=withdraw
    if withdraw>self.balance:
        print(f"Sorry,You cant withdraw this money beacuse your balance is {self.balance}")
    else:
        self.balance-=withdraw
        self.withdraws+=1
        print(f"The money has been withdrawn successfully\n")
        print(f"The new balance is {self.balance}")

  def transfer(self,t):
    self.t=t
    if t>self.balance:
      print(f"Sorry,You cant transfer this money beacuse your balance is {self.balance}")
    else:
      self.balance-=t
      self.transfers+=1
      print(f"The money has been transfered from this account successfully\n")
      print(f"The new balance is {self.balance}")

  def details(self):
    print(f"Hello,MR.{self.name}\nYour ID is {self.id}\nYour balance is {self.balance} ")

  def transactions(self):
    print(f"The number of deposits {self.deposits}\nThe number of withdraws {self.withdraws}\nThe number of transfers between accounts is {self.transfers}  ")             
  


print("Welcome to D R A G O N bank \nFirst,Please Create an account to enjoy our services")
while True:

    print("  ┌────────────────┐  ╭─────────────────────────────────────────╮     ")
    print("  │  ╭┼┼╮          │  │ ▶︎ 1 • Create Account                   │     ")
    print("  │  ╰┼┼╮          │  ├─────────────────────────────────────────|     ")
    print("  │  ╰┼┼╯          │  │ ▶︎ 2 • To Deposit                       │     ")
    print("  │                │  ├─────────────────────────────────────────|     ")
    print("  │  D R A G O N   │  │ ▶︎ 3 • To withdraw                      │     ")
    print("  │  B A N K       │  ├─────────────────────────────────────────|     ")
    print("  │                │  │ ▶︎ 4 • To transfer between accounts     │     ")
    print("  │                │  ├─────────────────────────────────────────|     ")
    print("  │                │  │ ▶ 5 • To show details of the account   │     ")
    print("  │                │  ├─────────────────────────────────────────|     ")
    print("  │ ║│┃┃║║│┃║│║┃│  │  │ ▶︎ 6 • To show all transactions         │     ")
    print("  │ ║│┃┃║║│┃║│║┃│  │  ├─────────────────────────────────────────|     ")
    print("  │                │  │ ▶︎ 7 • Exit System                      │     ")
    print("  └────────────────┘  ╰─────────────────────────────────────────╯     ")

    user_input=int(input("Enter the option number you want\n"))

    if user_input==7:
        break

    elif user_input==1:
        name=input("Please,Enter Your name\n")
        id=int(input("Please,Enter Your ID\n"))
        b1=Bank(name,id,0000)
        print("Account created successfully\n")

    elif user_input==2:
      deposit=int(input("Please,Enter the amount you want to deposit\n"))
      b1.deposit(deposit)

    elif user_input==3:
        withdraw=int(input("Please,Enter the amount you want to withdraw\n"))
        b1.withdraw(withdraw)

    elif user_input==4:
          t=int(input("Please,Enter the amount you want to transfer to another account\n"))
          b1.transfer(t)

    elif user_input==5:
      b1.details()

    elif user_input==6:
        b1.transactions()