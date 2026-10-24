import json
class Phone_book:
    def __init__(self,name,city,phone):
        self.name=name
        self.city=city
        self.phone=phone
    def input_data(self,contacts):
        contacts[self.name]={"city":self.city,"phone":self.phone}
        with open("cont_file2.json","w")as file:
            json.dump(contacts,file)
        print("phone book updated successfully")
    def receive_data(self,contacts):
        name=input("enter a name to find information")
        info=contacts.get(name,f"{name} is not in phone book")
        print(info)