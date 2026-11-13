from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
tree_model=DecisionTreeClassifier(max_depth=3,random_state=42)
tree_model.fit(x_train,y_train)
tree_predictions=tree_model.predict(x_test)
tree_accuracy=accuracy_score(y_test,tree_predictions)
print(f"tree_accuracy is: {tree_accuracy*100:.2f}%")
forest_model=RandomForestClassifier(n_estimators=100,max_depth=3,random_state=42)
forest_model.fit(x_train,y_train)
forest_predictions=forest_model.predict(x_test)
forest_accuracy=accuracy_score(y_test,forest_predictions)
print(f"forest_accuracy is: {forest_accuracy*100:.2f}%")
#%%
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
x,y=make_moons(n_samples=1000,noise=.3,random_state=42)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
tree_model=DecisionTreeClassifier(max_depth=3,random_state=42)
tree_model.fit(x_train,y_train)
tree_train_predict=tree_model.predict(x_train)
tree_test_predict=tree_model.predict(x_test)
tree_train_accuracy=accuracy_score(y_train,tree_train_predict)
tree_test_accuracy=accuracy_score(y_test,tree_test_predict)
forest_model=RandomForestClassifier(max_depth=3,n_estimators=100,random_state=42)
forest_model.fit(x_train,y_train)
forest_train_predict=forest_model.predict(x_train)
forest_test_predict=forest_model.predict(x_test)
forest_train_accuracy=accuracy_score(y_train,forest_train_predict)
forest_test_accuracy=accuracy_score(y_test,forest_test_predict)
print(f"tree train accuracy is: {tree_train_accuracy*100:.2f}% and tree test accuracy is: {tree_test_accuracy*100:.2f}%")
print(f"forest train accuracy is: {forest_train_accuracy*100:.2f}% and forest test accuracy is: {forest_test_accuracy*100:.2f}%")
# %%
