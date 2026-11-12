from sklearn.datasets import load_iris
import pandas as pd
iris=load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
print(df.head())
#%%
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd
iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
scaler=StandardScaler()
x_train_transformed=scaler.fit_transform(x_train)
x_test_transformed=scaler.transform(x_test)
model=KNeighborsClassifier(n_neighbors=3)
model.fit(x_train_transformed,y_train)
predictions=model.predict(x_test_transformed)
accuracy=accuracy_score(y_test,predictions)
cm=confusion_matrix(y_test,predictions)
print(f"accuracy is: {accuracy*100:.2f}%")
print(cm)
# %%
