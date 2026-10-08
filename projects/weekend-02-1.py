import json
def new_contact(phone_book):
    try:
        n=int(input("howmany contacts do you want to enter?"))
        for i in range(n):
            while True:
                try:
                    name=input("enter a new name")
                    phnumber=int(input("enter the phone number"))
                    city=input("enter city")
                    mail=input("enter email")
                    phone_book[name]={"phnumber":phnumber,"city":city,"mail":mail}
                    with open("projects/test1.json","w")as file:
                        json.dump(phone_book,file)
                    break    
                except ValueError: 
                    print("enter valid number")
    except ValueError:  
        print("enter valid number")
def contact_search(phone_book,name):
    info=phone_book.get(name,f"{name} is not in contacts")
    print(f"{name}'s information is: {info}")
def ind_city(phone_book):
    set1=set()
    for key,values in phone_book.items():
        city=phone_book[key].get("city")
        if city:
            set1.add(city)
    print(f"indivisual cities are {set1}")
def contact_mail(phone_book):
    for key,values in phone_book.items():
        print(phone_book.get(key,{}).get("mail",f"there is not mail for {key}"))
try:
    phone_notebook={}
    with open("projects/test1.json","r")as file:
        phone_notebook=json.load(file)
except (FileNotFoundError,json.JSONDecodeError):
    print()
new_contact(phone_notebook)
key=input("enter a name to search information")
contact_search(phone_notebook,key) 
ind_city(phone_notebook)
contact_mail(phone_notebook) 