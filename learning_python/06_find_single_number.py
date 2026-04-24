# 找出只出現一次的數字
def judge_apear(x, seq):
    if not isinstance(x, int):
        return None
    for i in seq:
        if x == i:
            return True
    return False
        
def unique(seq):
    if not isinstance(seq, list) or len(seq) < 2:
        return None
    unique = []
    for i in seq:
        if not judge_apear(i, unique):
            unique.append(i)
    return unique

def find_single(seq):
    unique_val = unique(seq)
    time = []
    single = []
    for i in unique_val:
        count = 0
        for j in seq:
            if i == j:
                count = count +1
        time.append(count)
    for i in range(0, len(time)):
        if time[i] == 1:
            single.append(unique_val[i])
    return single
    
if __name__ == "__main__":
    x = [2, 2, 1]
    y = [4, 1, 2, 1, 2]
    # z = 3
    # print(judge_apear(z, y))
    print(find_single(x))
    print(find_single(y))