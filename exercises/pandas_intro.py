import pandas as pd
scores=pd.Series([15,18,12,20])
print("scores:",scores)
#%%
import pandas as pd
data={"name":["Ali","Sara","Reza","Bahareh"],"age":[25,22,28,45],"city":["tehran","shiraz","mashhad","tehran"]}
df=pd.DataFrame(data)
print(df)
print()
print(df.info())
#%%
import pandas as pd
books={"name":["rebeka","majelan","anakarnina"],"pages":[456,380,1200],"author":["jan","duma","tolstoy"]}
books_data=pd.DataFrame(books)
print(books_data)
print()
print(books_data.head(2))
print()
print(books_data.describe())
print(books_data["name"])
print(books_data[books_data["author"]=="duma"])
#%%
import pandas as pd
data={"name":["Ali","Sara","Reza","Bahareh"],"age":[25,22,28,45],"city":["tehran","shiraz","mashhad","tehran"],"scores":[18,15,12,20]}
df=pd.DataFrame(data)
df.to_csv("students.csv",index=False)
data_csv=pd.read_csv("students.csv")
print(data_csv)
print(data_csv.head(3))
print(data_csv.describe())
print(data_csv["age"])
print(data_csv[data_csv["age"]>25])
#%%
import pandas as pd
df=pd.read_excel("friends.xlsx")
print(df)

# %%
