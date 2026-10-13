class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        if amount>=0:
            self.__balance+=amount
            b=self.__balance
            with open("projects/balance.txt","w")as file:
                                file.write(str(b)) 
        else:
            print("amount of deposit can't be negative")
           
    def withdrow(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            b=self.__balance
            with open("projects/balance.txt","w")as file:
                                file.write(str(b)) 
        else:
            print("amount of withdrow can't be more than balance")
    def get_balance(self):
        a=self.__balance
        print(f"{self.name}'s balance is {self.__balance}")
        return a
b=0    
try:
    with open("projects/balance.txt","r")as file:
        b=file.read()
except FileNotFoundError:
    print()            
name="Bahareh"
customer1=BankAccount(name,int(b))
while True:
        try:
            operation=input("for deposit enter d, for withdrow enter w, for get balance enter b,for exit entr e")
            if operation=="d":
                a=int(input("enter amount of deposit"))
                customer1.deposit(a)
            elif operation=="w":
                a=int(input("enter amount of withdrow"))
                customer1.withdrow(a)
            elif operation=="b":
                customer1.get_balance()
            elif operation=="e":
                  break    
            else:    
                print("enter valid operation")
        except ValueError:
            print("enter valid amount")  