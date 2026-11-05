import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class StoreAnalayzer:
    def __init__(self,data):
        self.data=data
    def data_cleaning(self):
        print("*is there duplicate data*")
        print(self.data.duplicated(subset=["Product","Category","Price","Quantity","CustomerCity","Discount"]).sum())
        print("*delet duplicated*")
        df2=self.data.drop_duplicates(subset=["Product","Category","Price","Quantity","CustomerCity","Discount"])
        print(df2)
        print("*fill empty cells*")
        df2["Discount"]=df2["Discount"].fillna(0)
        df2["CustomerCity"]=df2["CustomerCity"].fillna("UnKnown")
        print(df2)
    def data_analaysis(self):
        print("*price average for each category*")
        df2=self.data.drop_duplicates(subset=["Product","Category","Price","Quantity","CustomerCity","Discount"])
        s1=df2.groupby("Category")["Price"].mean()
        print(s1)
        print("*total sales count for each city*")
        s2=df2.groupby("CustomerCity")["Quantity"].sum()
        print(s2) 
    def visualisation(self):
        df2=self.data.drop_duplicates(subset=["Product","Category","Price","Quantity","CustomerCity","Discount"])
        s1=df2.groupby("Category")["Price"].mean()
        s2=df2.groupby("CustomerCity")["Quantity"].sum()
        plt.figure(figsize=(8,4))
        plt.bar(s1.index,s1.values,color=["blue","orange","purple"])
        plt.title("price average for each category")
        plt.xlabel("category")
        plt.ylabel("price average")
        plt.grid(True)
        plt.show()
        plt.figure(figsize=(8,4))
        plt.plot(s2.index,s2.values,color="blue",marker="o",linestyle="-",linewidth="2")
        plt.title("total sales count for each city")
        plt.xlabel("city")
        plt.ylabel("sales count")
        plt.grid(True)
        plt.show()
df=pd.read_csv("store_sales.csv")
print("*basic table*")
obj1=StoreAnalayzer(df)
obj1.data_cleaning()
obj1.data_analaysis()
obj1.visualisation()


        








 


