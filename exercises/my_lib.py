def students(name,age):
    print(f"name:{name}, age:{age}")
def salary(age,s):
    print(f"salary for {age} years old is {s}")
class Introduce:
    def __init__(self,name,job):
        self.name=name
        self.job=job
    def present(self):
        print(f"hello,my name is {self.name}. I'm a {self.job}")           