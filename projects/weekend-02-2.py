import json
class Phonebook:
    def __init__(self,contacts):
        self.contacts=contacts
    def add_contact(self):
        try:
            n=int(input("how many contacts do you want to enter?"))
            for i in range(n):
                while True:
                    try:
                        name=input("enter a new name")
                        phone=int(input("enter the phone number"))
                        self.contacts[name]=phone
                        break
                    except ValueError:
                        print("enter valid number")
            with open("projects/test2.json","w")as file:
                json.dump(self.contacts,file)            
        except ValueError:
            print("enter valid number") 
    def show_all(self):
        for key,value in self.contacts.items():
            print(f"{key}:{value}") 
    def find_key(self):
        key=input("enter a name to search for phone number")
        if key in self.contacts:
            print(f"{key}'s phone number is {self.contacts[key]}")
        else:
            print(f"there is not phone number for {key}")                    
try:
    pre_phonebook={}
    with open("projects/test2.json","r")as file:
        pre_phonebook=json.load(file)
except (FileNotFoundError,json.JSONDecodeError):
    print()
phonebook1=Phonebook(pre_phonebook)
phonebook1.add_contact()
phonebook1.show_all()
phonebook1.find_key()