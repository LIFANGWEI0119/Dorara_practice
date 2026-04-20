
#%%import numpy as np 
 
x =  [(1,2 , 3),(4,5)] 
a = np.asarray(x)  
print (a)
print(x)

#%%
import numpy as np 
 
# 使用 range 函数创建列表对象  
list=range(5)
it=iter(list)

# 使用迭代器创建 ndarray 
x=np.fromiter(it, dtype=float, count = -1)
print(list)
print(x)
print(it)

#%%
import numpy as np 
 
x =  (1,2,3) 
a = np.asarray(x)  
print (a)
# %%
