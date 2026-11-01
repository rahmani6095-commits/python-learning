import pandas as pd
import numpy as np
data={"name":["ali","sara","reza","sara","bahareh","maryam"],
      "age":[25,22,np.nan,22,45,19],
      "city":["tehran","shiraz","mashhad","shiraz","tehran",np.nan]}
df=pd.DataFrame(data)
print(df)
print("is there empty data?")
print(df.isnull().sum())
print("delet empty data")
df_no_null=df.dropna()
print(df_no_null)
print("is there duplicated data?")
print(df_no_null.duplicated().sum())
print("delet duplicated data")
clean_df_data=df_no_null.drop_duplicates()
print(clean_df_data)
#%%
import pandas as pd
import numpy as np
data={"name":["ali","sara","reza","bahareh"],
      "age":[25,np.nan,28,45],
      "city":["tehran","shiraz",np.nan,"tehran"]}
df=pd.DataFrame(data)
print("basic table")
print(df)
mean_age=df["age"].mean()
print("age average:",mean_age)
df["age"]=df["age"].fillna(mean_age)
df["city"]=df["city"].fillna("unknown")
print("table after filling")
print(df)
print("number of empty data:",df.isnull().sum().sum())
# %%
