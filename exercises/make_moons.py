import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
x,y=make_moons(n_samples=1000,noise=0,random_state=42)
plt.figure(figsize=(8,5))
plt.scatter(x[y==0,0],x[y==0,1],color="blue",label="class 0",alpha=.6)
plt.scatter(x[y==1,0],x[y==1,1],color="orange",label="class 1",alpha=.6)
plt.title("Make Moons Dataset (noise 0)")
plt.xlabel("feature 1")
plt.ylabel("feature 2")
plt.show()
#%%
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
x,y=make_moons(n_samples=1000,noise=.3,random_state=42)
plt.figure(figsize=(8,5))
plt.scatter(x[y==0,0],x[y==0,1],color="blue",label="class 0",alpha=.6)
plt.scatter(x[y==1,0],x[y==1,1],color="orange",label="class 1",alpha=.6)
plt.title("Make Moons Dataset (noise 0.3)")
plt.xlabel("feature 1")
plt.ylabel("feature 2")
plt.show()
# %%
