from sklearn.preprocessing import StandardScaler
import numpy as np
x=np.array([
    [25,5000],
    [30,8000],
    [35,12000],
    [40,20000]])
scaler=StandardScaler()
scaler.fit(x)
print(f"mean= {scaler.mean_}")
print(f"deviation from the mean={scaler.scale_}")
x_transformed=scaler.transform(x)
print("x before scale")
print(x)
print("x after scale")
print(x_transformed)
#%%
from sklearn.preprocessing import StandardScaler
import numpy as np
x=np.array([
    [25,5000],
    [30,8000],
    [35,12000],
    [40,20000]])
scaler=StandardScaler()
x_transformed=scaler.fit_transform(x)
print("x before scale")
print(x)
print("x after scale")
print(x_transformed)
# %%
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np
x=np.array([[20,6000000],[40,8000000],[70,12000000],[80,13000000],[85,15000000],[90,20000000]])
y=np.array([1,0,1,0,0,1])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.25,random_state=42)
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_transformed=scaler.fit(x_test)
model=LogisticRegression()
model.fit(x_train_scaled,y_train)
predictions=model.predict(x_test)
accuracy=accuracy_score(y_test,predictions)
print(f"accuracy is {accuracy*100}:.2f")

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler
import numpy as np
x=np.array([[20,6000000],[40,8000000],[70,12000000],[80,13000000],[85,15000000],[90,20000000]])
y=np.array([1,0,1,0,0,1])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.25,random_state=42)
scaler=StandardScaler()
scaler.fit(x_train)
print(scaler.mean_)
print(scaler.scale_)
x_train_transformed=scaler.transform(x_train)
print(x_train_transformed)
x_test_transformed=scaler.transform(x_test)
print(x_test_transformed)
model=LogisticRegression()
model.fit(x_train_transformed,y_train)
predictions=model.predict(x_test_transformed)
print(f"real answer is:{y_test}")
print(f"model prediction is: {predictions}")
accuracy=accuracy_score(y_test,predictions)
print(f"accuracy is: {accuracy*100:.2f}%")
cm=confusion_matrix(y_test,predictions)
print(cm)
# %%
