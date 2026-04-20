
#%%#  defaultdict
# 通常在我們取用調用某個dict的key值的時候，都必須事先檢查這個key值是否存在
# 否則如果直接調用不存在的key值，會直接拋出一個KeyError，比如說：
#  統計一個list裡每個元素出現的個數：
a_list = ['a','b','x','a','a','b','z']
counter_dict = {}
for element in a_list:
    if element not in counter_dict:
        counter_dict[element] = 1
    else:
        counter_dict[element] += 1

#%%
# 建立一個一對多的multidict:
key_values = [('even',2),('odd',1),('even',8),('odd',3),('float',2.4),('odd',7)]

multi_dict = {}
for key,value in key_values:
    if key not in multi_dict:
        multi_dict[key] = [value]
    else:
        multi_dict[key].append(value)

#%%
from collections import defaultdict

better_dict = defaultdict(list) # default值以一個list()方法產生
check_default = better_dict['a']
print(check_default) # 會輸出list()方法產生的空串列[]

better_dict['b'].append(1) # [1] 
better_dict['b'].append(2) # [1,2] 
better_dict['b'].append(3) # [1,2,3]
check_default = better_dict['b']
print(better_dict['b'])
print(check_default)

#%%
from collections import defaultdict

multi_dict = defaultdict(list) 
key_values = [('even',2),('odd',1),('even',8),('odd',3),('float',2.4),('odd',7)]

for key,value in key_values:
    multi_dict[key].append(value)

print(multi_dict) # 會輸出defaultdict(<class 'list'>, {'float': [2.4], 'even': [2, 8], 'odd': [1, 3, 7]})
#%%
from collections import defaultdict

def zero():
    return 0

counter_dict = defaultdict(zero) # default值以一個zero()方法產生
a_list = ['a','b','x','a','a','b','z']

for element in a_list:
        counter_dict[element] += 1

print(counter_dict) # 會輸出defaultdict(<function zero at 0x7fe488cb7bf8>, {'x': 1, 'z': 1, 'a': 3, 'b': 2})
# %%
from collections import Counter

a_str = 'abcaaabccabaddeae'
counter = Counter(a_str) # 可直接由初始化的方式統計個數
print(counter)
print(counter.most_common(3)) # 輸出最常出現的3個元素
print(counter['a'])
print(counter['z']) # 對於不存在的key值給出default值0

counter.update('aaeebbc') # 可用update的方式繼續統計個數
print(counter)
# %%
counter = Counter(['a','a','n'])
counter = Counter({'a':2,'n':1})
counter = Counter(a=2,n=1) # 這3個初始化後的結果是相同的
# %%
