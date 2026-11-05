import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class StoreAnalayzer:
    def __init__(self,data):
        self.data=data
        self.cleaned_data=None
        self.s1=None
        self.s2=None
    def data_cleaning(self):
        print("*is there duplicate data*")
        print(self.data.duplicated(subset=["Product","Category","Price","Quantity","CustomerCity","Discount"]).sum())
        print("*delet duplicated*")
        df2=self.data.drop_duplicates(subset=["Product","Category","Price","Quantity","CustomerCity","Discount"])
        print(df2)
        print("*fill empty cells*")
        df2["Discount"]=df2["Discount"].fillna(0)
        df2["CustomerCity"]=df2["CustomerCity"].fillna("UnKnown")
        self.cleaned_data=df2
        print("data was cleaned")
    def data_analaysis(self):
        print("*price average for each category*")
        self.s1=self.cleaned_data.groupby("Category")["Price"].mean()
        print(self.s1)
        print("*total sales count for each city*")
        self.s2=self.cleaned_data.groupby("CustomerCity")["Quantity"].sum()
        print(self.s2) 
    def visualisation(self):
        plt.figure(figsize=(8,4))
        plt.bar(self.s1.index,self.s1.values,color=["blue","orange","purple"])
        plt.title("price average for each category")
        plt.xlabel("category")
        plt.ylabel("price average")
        plt.grid(True)
        plt.show()
        plt.figure(figsize=(8,4))
        plt.plot(self.s2.index,self.s2.values,color="blue",marker="o",linestyle="-",linewidth="2")
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


        








 


