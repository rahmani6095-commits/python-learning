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