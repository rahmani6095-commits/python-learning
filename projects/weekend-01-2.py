contacts={"bahareh":{"phnumber":1239,"city":"tehran","email":"b@g.com"},"sara":{"phnumber":1136,"city":"tehran","email":"s@g.com"},"ana":{"phnumber":1135,"city":"ilam","email":"a@g.com"}}
fc=contacts.get("mina","mina is not in contacts")
print(fc)
cities=set()
for key,value in contacts.items():
    city=contacts[key]["city"]
    cities.add(city)
print(f"cities are {cities}")
contacts["razieh"]={"phnumber":1243,"city":"karaj","email":"r@g.com"}
print(contacts)
for key,value in contacts.items():
    ph=contacts[key]["phnumber"] 
    ci=contacts[key]["city"]
    em=contacts[key]["email"]
    tc=(key,ph,ci,em)
    print(tc)
contacts["samira"]={"phnumber":1252,"city":"karaj"}    
print(contacts) 
for key,value in contacts.items():
    em=contacts.get(key,{}).get("email","email has not registered")
    print(f"{key} email is: {em}")
cset={"tehran","zahedan","ilam","rasht"}  
clis=[]  
for key,value in contacts.items():
    c=contacts[key]["city"] 
    if c in cset:
        clis.append(c)
cc=set(clis)        
print(f"common cities are: {cc}")



