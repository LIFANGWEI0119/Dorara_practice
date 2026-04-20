#%%
class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0
        
    def deposit(self, amount):  #存款動作: amount代表存入金額
        if amount <= 0:
            raise ValueError('must be positive')
        self.balance += amount
        
    def withdraw(self, amount): #取款動作: amount代表取款金額
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError('balance not enough')
        
acct1 = Account('123_456_789', 'Justin') #開一個帳戶
acct1.deposit(100)
acct1.withdraw(30)
print(acct1.number)
print(acct1.balance) #餘額是 70
#%%
class Rectangle:   
   def __init__(self,l=0,b=0,cost=0): #可以先給參數預設值
       self.length=l
       self.breadth=b
       self.unit_cost=cost
   def get_perimeter(self):
       return 2 * (self.length + self.breadth)   
   def get_area(self):
       return self.length * self.breadth   
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost
# breadth = 200 cm, length = 400 cm, 1 cm^2 cost=200
r = Rectangle(400,200,200)
#r.length = 400  r.breadth = 200  r.unit_cost = 200
print("Area of Rectangle: %s cm^2" % (r.get_area()))
print("Cost of rectangular field: %s " %(r.calculate_cost()))
#Area of Rectangle: 80000 cm^2
#Cost of rectangular field:  16000000
#%%
class Dog():
    def __init__(self, name, age):
        # 設定物件本身(self)屬性(.name/age)為外部參數(name/age)
        self.name = name
        self.age = age
    
    # 叫的方法
    def bark(self, times=1):
        return "汪" * times
    
    # 利用 @property，將方法設定為屬性
    # 你可以看到物件裡面，內部參數的傳遞都是靠self來傳
    @property
    def asHumanAge(self):
        return self.age * 7
        
park = Dog("Park", 3)
print(park.name)
print(park.age)
print(park.bark(3))
print(park.asHumanAge)
# 檢查park這個實例裡面，含有什麼屬性和方法
print(dir(park))
# %%
class Dog():
    Name = 'dog'

    def run(self):
        print(f"{self.Name} is running")

dorara = Dog()
print(dorara.Name)
dorara.run()
# %%
class Dog():
    def __init__(self, Name):
        self.Name = Name

    def run(self):
        print("%s is running" % self.Name)

dorara = Dog('popy')
print(dorara.Name)
dorara.run()
# %%
