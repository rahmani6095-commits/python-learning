import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data={"name":["ali","sara","reza","maryam","hasan","zahra","amir","neda"],
      "department":["It","HR","IT","Sales","IT","HR","Sales",np.nan],
      "age":[25,30,np.nan,28,35,27,22,29],
      "salary":[5000,4500,6000,4000,5500,4800,4200,3900]}
df=pd.DataFrame(data)
print("basic table")
print(df)
print("iloc")
print(df.iloc[0])
print("loc")
print(df.loc[0])
print("5 max salary")
df_sorted=df.sort_values(by="salary",ascending=False)
print(df_sorted.head(5))
print("column's name")
print(df.columns)
print("name and salary columns")
print(df[["name","salary"]])
print("5 first rows")
print(df.head(5))
print("filling empty cells")
df["department"]=df["department"].fillna("unknown")
df["age"]=df["age"].fillna(df["age"].mean())
print(df)
print("saving as cvs and xlsx")
df.to_csv("clean_data.cvs",index=False)
df.to_excel("clean_data.xlsx",index=False)
print("salary average for each department")
salary_ave=df.groupby("department")["salary"].mean()
print(salary_ave)
plt.Figure(figsize=(8,4))
plt.bar(salary_ave.index,salary_ave.values,color=["blue","orange","black","purple","red"])
plt.title("average salary by department")
plt.xlabel("department name")
plt.ylabel("deparment salary ave")
plt.show()
