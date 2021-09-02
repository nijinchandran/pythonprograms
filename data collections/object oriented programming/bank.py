class Bank:
    bname="SBI"
    def accCreate(self,accno,name):

        self.acno=acno
        self.name=name
        self.minimumbal=5000
        self.balance=self.minimumbal
    def depost(self,amt):
        self.amt=amt
        self.balance+=self.amt
        print("your ",Bank.bname,"account has been cedited with amt",self.amt)
        print("your current balance=",self.balance)
    def withdraw(selfself,amnt):
        self.amnt=amnt
        if self.amnt>self.balance:
            print("insufficient balance")
        else:
            print("account debited with",self.amnt)
            self.balance-=self.amnt
            print("available balance=",self.balance)

obj=Bank()
num=int(input("enter accno"))
obj.acCreate(123,'abc')
obj.deposit(2500)
obj.withdraw(1500)