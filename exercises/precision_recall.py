from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,classification_report
breast=load_breast_cancer()
x=breast.data
y=breast.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
model=LogisticRegression(max_iter=5000)
model.fit(x_train,y_train)
predictions=model.predict(x_test)
accuracy=accuracy_score(y_test,predictions)
precision=precision_score(y_test,predictions)
recall=recall_score(y_test,predictions)
print(f"accuracy= {accuracy*100:.2f}%")
print(f"precision= {precision*100:.2f}%")
print(f"recall={recall*100:.2f}%")
print("*final report*")
print(classification_report(y_test,predictions))
#%%
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,classification_report
breast=load_breast_cancer()
x=breast.data
y=breast.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
model=LogisticRegression(max_iter=5000)
model.fit(x_train,y_train)
predictions=model.predict(x_test)
accuracy=accuracy_score(y_test,predictions)
precision=precision_score(y_test,predictions,pos_label=0)
recall=recall_score(y_test,predictions,pos_label=0)
print(f"accuracy= {accuracy*100:.2f}%")
print(f"precision= {precision*100:.2f}%")
print(f"recall={recall*100:.2f}%")
print("*final report*")
print(classification_report(y_test,predictions))
# %%
