#%%
# 取得目前工作目錄
import os
print(os.getcwd())

#%%
# 取得目前工作目錄的絕對路徑
import os
print(os.path.abspath('.'))
print(os.path.abspath('demo_silf.py'))

#%% 檢查路徑是否存在
path = os.path.abspath('.')

os.path.exists(path) # 判斷路徑是否存在
os.path.isabs(path) # 判斷路徑是否為絕對路徑
os.path.isdir(path) # 判斷路徑是否為資料夾
os.path.isfile(path) # 判斷路徑是否為檔案

#%% 檔案與資料夾的操作
# os.mkdir(path) # 建立path資料夾
# os.rmdir(path) # 刪除path的空資料夾
# os.chdir(path) # 將工作資料夾更改至path
# os.remove(path) # 刪除path檔案
# os.rename(old_path, new_path) # 將檔案更名為new_path

#%% 檔案讀取
# path = r"C:\Users\Dorara\Desktop\jena_climate_2009_2016.csv"
# path = "C:\\Users\\Dorara\\Desktop\\jena_climate_2009_2016.csv"
path = "C:/Users/Dorara/Desktop/jena_climate_2009_2016.csv"

file = open(path)
data = file.read()
file.close()

#%% CSV檔案處理 with Pandas
import pandas as pd
path = "C:/Users/Dorara/Desktop/jena_climate_2009_2016.csv"
df = pd.read_csv(path)