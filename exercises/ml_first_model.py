from sklearn.linear_model import LinearRegression
import numpy as np
x=np.array([[1],[2],[3],[4],[5]])
y=np.array([20,40,60,80,100])
model=LinearRegression()
model.fit(x,y)
print("model was been educated successfully and learned algorithem ")
new_data=np.array([[7]])
prediction=model.predict(new_data)
print(f"model predict for 7 hours study: {prediction[0]:.2f}")
#%%
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
x=np.array([[10,1],[15,0],[50,5],[100,10],[20,0],[80,8],[12,1],[90,9]])
y=np.array([0,0,1,1,0,1,0,1])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.25,random_state=42)
model=LogisticRegression()
model.fit(x_train,y_train)
predictions=model.predict(x_test)
accuracy=accuracy_score(y_test,predictions)
print(f"real answer: {y_test}")
print(f"model prediction: {predictions}")
print(f"accuracy: {accuracy*100:.2f}%")