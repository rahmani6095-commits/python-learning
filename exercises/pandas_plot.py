import pandas as pd
import matplotlib.pyplot as plt
data={"month":["jan","feb","march","apr","may"],
      "sales":[100,150,120,200,250]}
df=pd.DataFrame(data)
plt.figure(figsize=(8,4))
plt.plot(df["month"],df["sales"],marker="o",color="blue",linestyle="-",linewidth=2)
plt.title("sales over 5 month")
plt.xlabel("month")
plt.ylabel("sales")
plt.grid(True)
plt.savefig("sales_plot.png")
print("chart saved successfully")
plt.show() 
#%%
import pandas as pd
import matplotlib.pyplot as plt
data={"month":["jan","feb","march","apr","may"],
      "sales":[100,150,120,200,250]}
df=pd.DataFrame(data)
plt.Figure(figsize=(8,4))
plt.bar(df["month"],df["sales"],color=["blue","red","yellow","orange","purple"])
plt.title("sales bar chart")
plt.xlabel("month")
plt.ylabel("sales amount")
plt.show()
# %%
import pandas as pd
import matplotlib.pyplot as plt
data={"month":["jan","feb","march","apr","may"],
      "sales":[100,150,120,200,250]}
df=pd.DataFrame(data)
plt.figure(figsize=(8,4))
plt.plot(df["month"],df["sales"],marker="o",color="blue",linestyle="-",linewidth=2)
plt.title("sales over 5 month")
plt.xlabel("month")
plt.ylabel("sales")
plt.grid(True)
plt.show() 
plt.bar(df["month"],df["sales"],color=["blue","red","yellow","orange","purple"])
plt.title("sales bar chart")
plt.xlabel("month")
plt.ylabel("sales amount")
plt.show()
# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
age=np.random.randint(20,60,20)
salary=age*100+np.random.randint(-1000,1000,20)
df=pd.DataFrame({"age":age,"salary":salary})
plt.Figure(figsize=(8,4))
plt.scatter(df["age"],df["salary"],color="blue",alpha=.7)
plt.title("relationsheep between age and salary")
plt.xlabel("age")
plt.ylabel("salary")
plt.show() 
plt.Figure(figsize=(8,4))
plt.hist(df["salary"],bins=10,color="orange",edgecolor="blue")
plt.title("distribution of salaries")
plt.xlabel("salary range")
plt.ylabel("number of employee")
plt.show()
plt.Figure(figsize=(8,4))
plt.hist(df["age"],bins=10,color="green",edgecolor="red")
plt.title("distribution of age")
plt.xlabel("age range")
plt.ylabel("numbre of employee")
plt.show()

# %%
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("name frequency.xlsx")
print("TABLE")
print(df)
plt.figure(figsize=(8,4))
plt.plot(df["name"],df["frequency"],marker="o",color="blue",linestyle="-",linewidth=2)
plt.title("Name Frequency")
plt.xlabel("name")
plt.ylabel("frequency")
plt.grid(True)
plt.show()
plt.Figure(figsize=(8,4))
plt.bar(df["name"],df["frequency"],color=["blue","red","green","orange","purple","black","yellow","pink","brown","gray"])
plt.title("Name Frequency")
plt.xlabel("name")
plt.ylabel("frequency")
plt.show()
plt.Figure(figsize=(8,4))
plt.scatter(df["name"],df["frequency"],color="blue",alpha=.7)
plt.title("Name Frequency")
plt.xlabel("name")
plt.ylabel("frequency")
plt.grid(True)
plt.show()
plt.Figure(figsize=(8,4))
plt.hist(df["name"],color="blue",edgecolor="orange",bins=11)
plt.title("dist of name")
plt.xlabel("name")
plt.ylabel("count")
plt.show()

# %%

