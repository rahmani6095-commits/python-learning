phone_note={"Bahareh":1239,"Sara":1136,"razie":1241}
phone_note["Anita"]=1135
phone_note["Tahmineh"]=1245
del phone_note["Sara"]
print(phone_note)
l=len(phone_note)
print(f"number of contacts is {l}")
a=0
name=input("enter name").lower()
for key,value in phone_note.items():
    if key.lower()==name:
        print(f"{name} phone number is {value}")
        a=1
if a==0:
    print("there is no phone number for this name")   
#تغییر پیام کامیت         
