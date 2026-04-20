
#%%
# 賦值引用
a = {1: [1,2,3],0: [4, 5, 6]}
b = a
print(a, b)
# {1: [1, 2, 3], 0: [4, 5, 6]} {1: [1, 2, 3], 0: [4, 5, 6]}
a[1].append(4)
print(a, b)
# {1: [1, 2, 3, 4], 0: [4, 5, 6]} {1: [1, 2, 3, 4], 0: [4, 5, 6]}
print(a[0])
# [4, 5, 6]
#%%
# 淺拷貝
a = {1: [1,2,3]}
b = a.copy()
print(a, b)
# ({1: [1, 2, 3]}, {1: [1, 2, 3]})
a[1].append(4)
print(a, b)
# ({1: [1, 2, 3, 4]}, {1: [1, 2, 3, 4]})
# %%
# 深度拷貝需要引入copy 模組：
import copy 
c = copy . deepcopy ( a ) 
print(a , c)
# { 1 : [ 1 , 2 , 3 , 4 ] }, { 1 : [ 1 , 2 , 3 , 4 ] } 
a[1].append(5) 
print(a, c)
# { 1 : [ 1 , 2 , 3 , 4 , 5 ] }, { 1 : [ 1 , 2 , 3 , 4 ] }
#%%
from copy import deepcopy, copy
a = [80, 90]
b = [a, 100]
a.append(b)
print("a:", a)
print("b:", b)

c = deepcopy(a)
print("c:", c)

d = copy(b)
print("d:", d)
#%%
a = 1
b = a
print(id(a) == id(b))
# True
x = [1, 2, 3]
y = [x, 4]
print(x)
# [1, 2, 3]
print(y)
# [[1, 2, 3], 4]
print(id(x) == id(y))
# False
print(id(x) == id(y[0]))
# True
x[1] = 2020
print(x, y)
# [1, 2020, 3] [[1, 2020, 3], 4]
# %%
L = [2019, 2020, 2021]
D = {'1':2019, '2':2020, '3':2021}
 
A = L[:]  # 區分 A=L 或 A = List(L)
B = D.copy()  # 區分 B=D 
print(A)
# [2019, 2020, 2021]
print(B)
# {'1': 2019, '2': 2020, '3': 2021}
A[1] = 'happy'
B[3] = 'today'
print(L, D)
# ([2019, 2020, 2021], {'1': 2019, '2': 2020, '3': 2021})
print(A, B)
# ([2019, 'happy', 2021], {'1': 2019, '2': 2020, '3': 2021, 3: 'today'})
#%%
l1 = [3, [66, 55, 44], (3, 7, 21)]
l2 = list(l1)
l1.append(100)
print('l1:', l1)
# l1: [3, [66, 55, 44], (3, 7, 21), 100]
print('l2:', l2)
# l2: [3, [66, 55, 44], (3, 7, 21)]
l1[1].remove(55)
l2[1] += [33, 22]
l2[2] += (9, 9, 81)
print('l1:', l1)
# l1: [3, [66, 44, 33, 22], (3, 7, 21), 100]
print('l2:', l2)
# l2: [3, [66, 44, 33, 22], (3, 7, 21, 9, 9, 81)]
# %%
from copy import deepcopy
l1 = [3, [66, 55, 44], (3, 7, 21)]
l2 = deepcopy(l1)
l1.append(100)
print('l1:', l1)
# [3, [66, 55, 44], (3, 7, 21), 100]
print('l2:', l2)
# [3, [66, 55, 44], (3, 7, 21)]
l1[1].remove(55)
l2[1] += [33, 22]
l2[2] += (9, 9, 81)
print('l1:', l1)
# l1: [3, [66, 44], (3, 7, 21), 100]
print('l2:', l2)
# l2: [3, [66, 55, 44, 33, 22], (3, 7, 21, 9, 9, 81)]
#%%
import copy
a = [1, 2, 3, 4, ['a', 'b']] #原始对象
 
b = a                       #赋值，传对象的引用
c = copy.copy(a)            #对象拷贝，浅拷贝
d = copy.deepcopy(a)        #对象拷贝，深拷贝
 
a.append(5)                 #修改对象a
a[4].append('c')            #修改对象a中的['a', 'b']数组对象
 
print( 'a = ', a )
print( 'b = ', b )
print( 'c = ', c )
print( 'd = ', d )
#%%
from copy import deepcopy, copy
a = [80, 90]
b = [a, 100]
a.append(b)
print("a:", a)
# a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print("b:", b)
# b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
c = deepcopy(a)
print("c:", c)
# c =  [1, 2, 3, 4, ['a', 'b', 'c']]
d = copy(b)
print("d:", d)
# d =  [1, 2, 3, 4, ['a', 'b']]