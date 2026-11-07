from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
import numpy as np
x=np.array([[2],[5],[6],[4],[8],[12]])
y=np.array([13,31,37,25,49,73])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.25,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
predictions=model.predict(x_test)
mse=mean_squared_error(y_test,predictions)
r2=r2_score(y_test,predictions)
print(f"real answer is: {y_test}")
print(f"model predictions is: {predictions}")
print(f"mean squered errored (MSE): {mse:.2f}")
print(f"R2 score:{r2:.2f}")
#%%
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
import numpy as np
x=np.array([[1],[5],[4],[3],[2],[6]])
y=np.array([11,18,15,13,12,20])
model=LinearRegression()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.25,random_state=42)
model.fit(x_train,y_train)
predictions=model.predict(x_test)
mse=mean_squared_error(y_test,predictions)
r2=r2_score(y_test,predictions)
print(f"real answer is: {y_test}")
print(f"model prediction is: {predictions}")
print(f"MSE is: {mse}")
print(f"r2_score is: {r2}")
# %%
