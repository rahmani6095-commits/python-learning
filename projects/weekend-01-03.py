def contact_search(phone_notebook):
    name=input("enter a name")
    print(phone_notebook.get(name,f"{name} is not in phone_notebook"))
def ind_cities(phone_notebook):
    city_set=set()
    for key,value in phone_notebook.items():
        city=phone_notebook.get(key,{}).get("city",f"there is no city for {key}")
        city_set.add(city)
    print(f"cities in phone notebook are: {city_set}")  
def new_contact(phone_notebook):
    name=input("enter a name: ")
    phone_number=int(input("enter phone number"))
    city=input("enter city")
    mail=input("enter email")
    phone_notebook[name]={"phnumber":phone_number,"city":city,"email":mail}
    print(phone_notebook)   
def notebook_brief(phone_notebook):
    inf_tuple=()
    for key,value in phone_notebook.items():
        inf_tuple=(key,value)
        print(inf_tuple)
def contact_mail(phone_notebook):
    for key,value in phone_notebook.items():
        mail=phone_notebook.get(key,{}).get("email","email has not been registered for this one")
        print(f"mail for {key} is {mail}") 
def common_cities(phone_notebook,*city1):  
    city_set=set(city1) 
    city_set2=set()
    for key,value in phone_notebook.items():
        city=phone_notebook.get(key,{}).get("city","no city")
        city_set2.add(city)
    print(city_set & city_set2)          
phone_notebook={"bahareh":{"phnumber":1239,"city":"tehran","email":"b@g.com"},
                "sara":{"phnumber":1136,"city":"tehran","email":"s@g.com"},
                "ana":{"phnumber":1135,"city":"ilam","email":"a@g.com"}}    
contact_search(phone_notebook)
new_contact(phone_notebook)
ind_cities(phone_notebook)
contact_mail(phone_notebook)
common_cities(phone_notebook,"tehran","rasht")
notebook_brief(phone_notebook)
#finish