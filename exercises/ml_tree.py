from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
x=np.array([[20,2000],[25,3000],[30,5000],[35,8000],[40,12000],[45,15000],[50,20000],[55,25000]])
y=np.array([0,0,0,1,1,1,1,1])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.25,random_state=42)
model=DecisionTreeClassifier(max_depth=3,random_state=42)
model.fit(x_train,y_train)
predictions=model.predict(x_test)
accuracy=accuracy_score(y_test,predictions)
print(f"raal answer is: {y_test}")
print(f"model prediction is: {predictions}")
print(f"accuracy is {accuracy*100:.2f}%")
#%%
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
x=np.array([[20,2000],[25,3000],[30,5000],[35,8000],[40,12000],[45,15000],[50,20000],[55,25000],[20,3000]])
y=np.array([0,0,0,1,1,1,1,1,1])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.25,random_state=11)
model=DecisionTreeClassifier(max_depth=1,random_state=10)
model.fit(x_train,y_train)
predictions=model.predict(x_test)
accuracy=accuracy_score(y_test,predictions)
print(f"raal answer is: {y_test}")
print(f"model prediction is: {predictions}")
print(f"accuracy is {accuracy*100:.2f}%")
# %%
