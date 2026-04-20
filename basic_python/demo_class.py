#%%
class Animal():
 def __init__(self, name):
  self.name = name
a = Animal("dog")  #建立一個名叫dog的Animal實體(物件)
print(a.name)
# %%
# Cat的藍圖
class Cat:
 #建構子
    def __init__(self):
        self.color = 'Red' # 屬性(Attribute)
        self.legs = 'Long' # 屬性(Attribute)
    
    # 方法(Method)
    def run(self):
        print('Cat is running')
        
# Leo的藍圖
class Leo:
    # 建構子
    def __init__(self):
        self.color = 'Black' # 屬性(Attribute)
        self.legs = 'Short' # 屬性(Attribute)
    
    # 方法(Method)
    def eat(self):
        print('Leo is eatting')
        

Nash = Cat() # nask是Cat的具體化物件(object)
print(Nash.color)
Nash.run() # 使用物件裡面的方法

mary = Leo() # mary是Leo的具體化物件(object)
mary.eat() # 使用物件裡面的方法
# %%
class Father:
    def __init__(self):
        self.head = 'Big'
    
    def work(self):
        print('work hard')


# 此時Father就是Son的父類
# 也可以說Son繼承Father類
class Son(Father):
    def __init__(self):
        self.color = 'Red'
        self.legs = 'Long'
    
    def play(self):
        print('play hard')
        
        
nask = Son()
nask.work() # 繼承後就可以使用父類的屬性及方法
# %%
# Grandfather類
class Grandfather:
    def __init__(self):
        self.head = 'Big'
    
    def work(self):
        print('No work')
# Father繼承了Grandfather
class Father(Grandfather):
    def __init__(self):
        self.head = 'Big'
    
    def work(self):
        print('work hard')
class Mother:
    def __init__(self):
        self.head = 'Big'
    
    def work(self):
        print('No work')
# Son繼承了Father
class Son(Father):
    def __init__(self):
        self.color = 'Red'
        self.legs = 'Long'
    
    def play(self):
        print('play hard')
# Baby繼承Father及Monther類
class Baby(Mother, Father):
    def __init__(self):
        self.color = 'Red'
        self.legs = 'Long'
    
    def play(self):
        print('play hard')
nask = Son()
nask.work() # work hard
nask.play() # play hard
dorara = Baby()
dorara.work() # No work
dorara.play() # play hard
# %%
class Son:
    def __init__(self):
        self.color = 'Red'
        self.legs = 'Long'
        self.__IQ = '300'
    
    def play(self):
        print('play hard')
    
    def hungry(self):
        self.__eat()
    
    def __eat(self):
        print('good')
        
nask = Son()
nask.play() # play hard
nask.hungry() # good
nask.__eat() # 'Son' object has no attribute '__eat' 只能在類裡面自己呼叫用
nask.__IQ() # 'Son' object has no attribute '__IQ' 屬性也是一樣
#%%
# Cat的藍圖
class Cat:
    # 建構子
    def __init__(self):
        self.color = 'Red' # 屬性(Attribute)
        self.legs = 'Long' # 屬性(Attribute)
    
    # 方法(Method)
    def eat(self):
        print('Cat is eatting')
        
# Leo的藍圖
class Leo:
    # 建構子
    def __init__(self):
        self.color = 'Black' # 屬性(Attribute)
        self.legs = 'Short' # 屬性(Attribute)
    
    # 方法(Method)
    def eat(self):
        print('Leo is eatting')
        

nask = Cat() 
nask.eat() # Cat is eatting

mary = Leo() 
mary.eat() # Leo is eatting