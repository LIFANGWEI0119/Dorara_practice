def find_second_max_optimized(seq):
    # 1. 依然要做的安全檢查
    if not isinstance(seq, list) or len(seq) < 2:
        return None

    # 2. 初始化 (這次我們用 C 語言風格的極小值)
    max_val = float('-inf')
    sec_val = float('-inf')

    # 3. 只有一個迴圈，掃描全場
    for num in seq:
        if not isinstance(num, int): 
            return None

        if num > max_val:
            sec_val = max_val
            max_val = num
            pass
        elif num > sec_val and num != max_val:
            sec_val = num
            pass
            
    # 4. 最後的檢查：如果 sec_val 依然是負無限大，代表什麼？
    # (例如 seq = [9, 9, 9])
    if sec_val == float('-inf'):
        return None
        
    return sec_val