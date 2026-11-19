import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
url=url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df=pd.read_csv(url)
print("**5 TOP ROWS**")
print(df.head())
print("**INFORMATION**")
print(df.info())
print("**NUMBER OF EMPTY CELLS IN EACH COLUMN**")
print(df.isnull().sum())
print("**DELET COLUMN Cabin**")
df=df.drop(columns="Cabin")
print(df)
print("**DELET ROWS WITH EMPTY CELLS IN COLUMN Embarked**")
df=df.dropna(subset="Embarked")
print(df.isnull().sum())
print("**FILL EMPTY CELLS IN COLUMN Age**")
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df.isnull().sum())
print("**DELET INEFFICIENT COLUMNS**")
df=df.drop(columns=["PassengerId","Name","Ticket"])
print(df.info)
print("**CONVERT SEX AND Embarked TO NUMBER**")
df["Sex"]=df["Sex"].map({"male":0,"female":1})
df["Embarked"]=df["Embarked"].map({"C":0,"Q":1,"S":2})
print(df.head())
print("**SPLIT DATA IN FEATURES AND TARGET**")
x=df.drop(columns="Survived")
y=df["Survived"]
print(x)
print(y)
print("**SPLIT DATA IN TRAIN AND TEST**")
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
print("**DATA SCALING**")
scaler=StandardScaler()
x_train_transform=scaler.fit_transform(x_train)
x_test_transform=scaler.transform(x_test)
print("**MODEL BUILDING AND TRAINING**")
model=LogisticRegression(max_iter=5000)
model.fit(x_train_transform,y_train)
print("**PREDICTION, ACCURACY AND CONFUSION MATRIX**")
predictions=model.predict(x_test_transform)
accuracy=accuracy_score(y_test,predictions)
cm=confusion_matrix(y_test,predictions)
print(f"acuuracy is: {accuracy*100:.2f}%")
print(f"confusion matrix is: {cm} ")
#%%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.ensemble import RandomForestClassifier
url=url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df=pd.read_csv(url)
print("**5 TOP ROWS**")
print(df.head())
print("**INFORMATION**")
print(df.info())
print("**NUMBER OF EMPTY CELLS IN EACH COLUMN**")
print(df.isnull().sum())
print("**DELET COLUMN Cabin**")
df=df.drop(columns="Cabin")
print(df)
print("**DELET ROWS WITH EMPTY CELLS IN COLUMN Embarked**")
df=df.dropna(subset="Embarked")
print(df.isnull().sum())
print("**FILL EMPTY CELLS IN COLUMN Age**")
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df.isnull().sum())
print("**DELET INEFFICIENT COLUMNS**")
df=df.drop(columns=["PassengerId","Name","Ticket"])
print(df.info)
print("**CONVERT SEX AND Embarked TO NUMBER**")
df["Sex"]=df["Sex"].map({"male":0,"female":1})
df["Embarked"]=df["Embarked"].map({"C":0,"Q":1,"S":2})
print(df.head())
print("**SPLIT DATA IN FEATURES AND TARGET**")
x=df.drop(columns="Survived")
y=df["Survived"]
print(x)
print(y)
print("**SPLIT DATA IN TRAIN AND TEST**")
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
print("**MODEL BUILDING AND TRAINING**")
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(x_train,y_train)
print("**PREDICTION, ACCURACY AND CONFUSION MATRIX**")
predictions=model.predict(x_test)
accuracy=accuracy_score(y_test,predictions)
cm=confusion_matrix(y_test,predictions)
print(f"acuuracy is: {accuracy*100:.2f}%")
print(f"confusion matrix is: {cm} ")
#%%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.ensemble import RandomForestClassifier
url=url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df=pd.read_csv(url)
print("**5 TOP ROWS**")
print(df.head())
print("**INFORMATION**")
print(df.info())
print("**NUMBER OF EMPTY CELLS IN EACH COLUMN**")
print(df.isnull().sum())
print("**DELET COLUMN Cabin**")
df=df.drop(columns="Cabin")
print(df)
print("**DELET ROWS WITH EMPTY CELLS IN COLUMN Embarked**")
df=df.dropna(subset="Embarked")
print(df.isnull().sum())
print("**FILL EMPTY CELLS IN COLUMN Age**")
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df.isnull().sum())
print("**DELET INEFFICIENT COLUMNS**")
df=df.drop(columns=["PassengerId","Name","Ticket"])
print(df.info)
print("**CONVERT SEX AND Embarked TO NUMBER**")
df["Sex"]=df["Sex"].map({"male":0,"female":1})
df["Embarked"]=df["Embarked"].map({"C":0,"Q":1,"S":2})
print(df.head())
print("**BUILDING COLUMN FamilySize**")
df["FamilySize"]=df["SibSp"]+df["Parch"]+1
df=df.drop(columns=["SibSp","Parch"])
print(df)
print("**SPLIT DATA IN FEATURES AND TARGET**")
x=df.drop(columns="Survived")
y=df["Survived"]
print(x)
print(y)
print("**SPLIT DATA IN TRAIN AND TEST**")
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
print("**MODEL BUILDING AND TRAINING**")
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(x_train,y_train)
print("**PREDICTION, ACCURACY AND CONFUSION MATRIX**")
predictions=model.predict(x_test)
accuracy=accuracy_score(y_test,predictions)
cm=confusion_matrix(y_test,predictions)
print(f"acuuracy is: {accuracy*100:.2f}%")
print(f"confusion matrix is: {cm} ")
#%%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import joblib
url=url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df=pd.read_csv(url)
print("**5 TOP ROWS**")
print(df.head())
print("**INFORMATION**")
print(df.info())
print("**NUMBER OF EMPTY CELLS IN EACH COLUMN**")
print(df.isnull().sum())
print("**DELET COLUMN Cabin**")
df=df.drop(columns="Cabin")
print(df)
print("**DELET ROWS WITH EMPTY CELLS IN COLUMN Embarked**")
df=df.dropna(subset="Embarked")
print(df.isnull().sum())
print("**FILL EMPTY CELLS IN COLUMN Age**")
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df.isnull().sum())
print("**DELET INEFFICIENT COLUMNS**")
df=df.drop(columns=["PassengerId","Name","Ticket"])
print(df.info)
print("**CONVERT SEX AND Embarked TO NUMBER**")
df["Sex"]=df["Sex"].map({"male":0,"female":1})
df["Embarked"]=df["Embarked"].map({"C":0,"Q":1,"S":2})
print(df.head())
print("**BUILDING COLUMN FamilySize**")
df["FamilySize"]=df["SibSp"]+df["Parch"]+1
df=df.drop(columns=["SibSp","Parch"])
print(df)
print("**BUILDING COLUMN IsAlone**")
df["IsAlone"]=np.where(df["FamilySize"]==1,1,0)
print(df.head())
print("**SPLIT DATA IN FEATURES AND TARGET**")
x=df.drop(columns="Survived")
y=df["Survived"]
print(x)
print(y)
print("**SPLIT DATA IN TRAIN AND TEST**")
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
print("**MODEL BUILDING AND TRAINING**")
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(x_train,y_train)
print("**PREDICTION, ACCURACY AND CONFUSION MATRIX**")
predictions=model.predict(x_test)
accuracy=accuracy_score(y_test,predictions)
cm=confusion_matrix(y_test,predictions)
print(f"acuuracy is: {accuracy*100:.2f}%")
print(f"confusion matrix is: {cm} ")
joblib.dump(model,"titanic1_model.pkl")
#%%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import joblib
data={"Pclass":1,"Sex":1,"Age":25,"Fare":70,"Embarked":0,"FamilySize":2,"IsAlone":0}
x=pd.DataFrame([data])
loaded_model1=joblib.load("titanic1_model.pkl")
prediction=loaded_model1.predict(x)
print(prediction)
# %%
