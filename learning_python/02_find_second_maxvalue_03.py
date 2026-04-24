def find_secondmax(x):
    # 1. 基本檢查
    if not isinstance(x, list) or len(x) < 2:
        return None
       
    # 2. 去除重複並確保還是有兩個以上不同的數
    unique_x = list(set(x))
    if len(unique_x) < 2:
        return None # 如果全部數字都一樣，就沒有第二大
    
    # 3. 初始化 (直接拿前兩個不同的數來比就好)
    max_val = float('-inf')
    second_val = float('-inf')
    
    # 4. 只有一個迴圈，乾乾淨淨
    for num in unique_x:
        if num > max_val:
            second_val = max_val
            max_val = num
        elif num > second_val:
            second_val = num            
    return second_val

if __name__ == "__main__":
    x = [9, 9, 2, 9, 5, 1, 7]
    print(find_secondmax(x))
