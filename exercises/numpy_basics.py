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
#%%
import numpy as np
scores=np.array([12,18,15,20,8,16,14])
mask=scores>=15
print(mask)
print(scores[mask])
#%%
import numpy as np
scores=np.array([11,16,19,17,20,12])
print(scores[scores>=15])
#%%
import numpy as np
mat=np.array([[11,15,46],[52,26,3],[19,78,14]])
print(mat[mat>20])


# %%
import numpy as np
arr=np.arange(1,13)
print("arr:",arr)
mat=arr.reshape(3,4)
print("mat=reshaped arr:",mat)
flatten_mat=mat.flatten()
print("reflaten arr:",flatten_mat)



# %%
import numpy as np
team_a_scores=np.array([10,20,30])
team_b_scores=np.array([40,50,60])
combined_scores=np.concatenate((team_a_scores,team_b_scores))
print("combined arrays:",combined_scores)

# %%
import numpy as np
arr2=np.array([[1,2,3],[4,5,6]])
auto_reshaped_arr=arr2.reshape(3,-1)
print("auto_reshaped_arr:",auto_reshaped_arr)

# %%
import numpy as np
arr=np.arange(1,13)
print("arr:",arr)
mat=arr.reshape(3,4)
print("mat=reshaped arr:",mat)
flatten_mat=mat.reshape(1,-1)
print("reflaten arr:",flatten_mat)


# %%
import numpy as np
random_float=np.random.rand(4)
print(random_float)
#%%
np.random.seed(42)
print(np.random.randint(1,100,5))
np.random.seed(42)
print(np.random.randint(1,100,5))
#%%
data=np.arange(1,11)
print(data)
np.random.shuffle(data)
print(data)
#%%
data=np.arange(1,101)
np.random.shuffle(data)
print(data)
train_data=data[:80]
test_data=data[80:]
print(train_data)
print(test_data)
print(len(train_data))
print(len(test_data))

