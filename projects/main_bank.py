from bank_account import BankAccount
def run_bank_app():
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
if __name__=="__main__":
     run_bank_app()            