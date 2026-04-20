#%%
class Cat:
    def __init__():
        color = 'Red'
        legs = 'Long'
    def run():
        print('Cat is running')

Cat.run() # Cat is running
#%%
class Cat:
    def __init__(self):
        self.color = 'Red'
        self.legs = 'Long'
    
    def run(self):
        print('Cat is running', self.legs) # 可以在同一類中呼叫有冠上self的變數及方法
        
nask = Cat() # 先創具體化物件
nask.run() # Cat is running Long
#%%
class Cat:
    def __init__(self):
        self.color = 'Red'
        self.legs = 'Long'
        print('Cat say hi')
    
    def run(self):
        print('Cat is running', self.legs) # 可以在同一類中呼叫有冠上self的變數及方法
        
nask = Cat() # 先創具體化物件
nask.run() # Cat is running Long

'''執行
Cat say hi
Cat is running Long
'''
#%%
class Cat:
    def __init__(self, name):
        self.color = 'Red'
        self.legs = 'Long'
        self.name = name
        print('Cat say hi')
    
    def run(self):
        print('Cat is running', self.legs)
        print(self.name)
        
nask = Cat('mumu') # __init__的參數具體化物件時要先給
nask.run() # Cat is running Long

# '''執行
# Cat say hi
# Cat is running Long
# mumu
# '''
#%%
#上面不懂的話我再補充一個舉例
# 譬如狗的話 你可以新增他的類別
# class Dog():
# 屬性則是名字、年齡、血型、喜歡的食物等
# 可以這樣加入屬性
# 這邊用中文闡述def __init__的過程
# def __init__(self,名字,年齡)
# 因為self是class本身 所以第一個不用更動
# 接下來再設定
# self.名字=名字
# self.年齡=年齡
# 在這邊self.的設定 就代表你之後可以用的class屬性
# 所以我之後就可以用
# 來福 = Dog(來福,8) 
# 讓來福變成是一種dog類別的物件
# 並且具有名字屬性跟年齡屬性 所以
# print 來福.年齡 就會出現8