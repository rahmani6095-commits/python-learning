import numpy as np
my_array=np.array([1,2,3,4,5])
print(my_array)
my_array2=np.arange(1,6)
print(my_array2)
print(np.zeros(5))
print(np.ones(5))
#%%
import numpy as np
mat1=np.array([[1,2,3],[4,5,6]])
print(mat1)
print(mat1.shape)
print(mat1.ndim)
mat2=mat1.reshape(3,2)
print(mat2)
print(mat2[2,1])
print(mat2[:,0])
print(mat2[1,:])
#%%
import numpy as np
data=np.array([[10,20,30],[40,50,60]])
print("sum for all numbers:",np.sum(data))
print("average for all numbers:",np.mean(data))
print("maximum number:",np.max(data))
print("sum for each column:",np.sum(data,axis=0))
print("sum for each row:",np.sum(data,axis=1))
