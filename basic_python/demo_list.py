#%%
L=[0]*2 
#output:L=[0,0]
L.append(3) 
#output:L=[0,0,3]
K=[0,0,3,4,1,2]
K.pop(4) 
#output:L=[0,0,3,4,2]
K.count('3') 
#output:0
del(L[2]) 
#output:L=[0,0,4,2]
#%%
L=[3,4,5,7,8,9] 
L[-3] #output:7
L=[3,4,5,7,8,9] 
L.pop() #output:L=[3,4,5,7,8]
#%% range(start,end,step)可以從start到end之前(不包含end)，以step為間隔的整數數列
L=[1,5,2,7,8,4] 
L[1:4] #output:[5,2,7]
L[1:] #output:[5,2,7,8,4]
L[1::] #output:[5,2,7,8,4]
L[:4] #output:[1,5,2,7] 
L[::4] #output:[1,8]
#%% 二維陣列 2-D list
import numpy as np
A=[[0,1,2,3,4],[1,11,21,31,41],[2,12,22,32,42],[3,13,23,33,43]] #2-D list
print(A[1]) #output:[1,11,21,31,41]
print(A[2][3]) #output:32
print(len(A))  #output:4
print(len(A[3]))  #output:5
print(np.shape(A))  #output:(4,5) #先row再col.
#%%
import numpy as np
B=np.random.randint(1,30,(3,3,3))
#[[[ 9 11 11]
#  [20 26 25]
#  [ 5 22 14]]
#上面為page0
# [[ 5  6 13]
#  [ 2  9 14]
#  [ 8 19  4]]
#上面為page1
# [[ 3 17  7]
#  [21 28 27]
#  [19  6 22]]]
#上面為page2
print(np.shape(B))  #output:(3,3,3) #先row再col.
print(len(A))  #output:3
print(B[2][1]) #output:[21, 28, 27]
print(B[1][2][0]) #output:8