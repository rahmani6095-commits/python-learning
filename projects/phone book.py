import json
from phone_class import Phone_book
contacts={}
try:
    with open("cont_file2.json","r")as file:
        contacts=json.load(file)
except FileNotFoundError:
    print()
while True:
    op=input("for input new contact type i, for find information type r, for exit type e ")
    if op=="i":
        try:
            name=input("enter name")
            city=input("enter city")
            phone=int(input("enter phone number"))
            contact1=Phone_book(name,city,phone)
            contact1.input_data(contacts)
        except ValueError:
            print("enter valid number")
    elif op=="r":
        c=Phone_book("","",0)
        c.receive_data(contacts)
    elif op=="e":
        break
    else:
        print("choose valid operation")                            
