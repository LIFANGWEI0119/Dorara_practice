# 相較_01改進的地方符合「找出第二大數」的需求，且能處理重複數字

def find_secondmax(x):
    if not isinstance(x, list) or len(x) < 2:
        return None
    n = len(x)
    for i in range(0, n):
        if not isinstance(x[i], int):
            return None
        if i == 0:
            max = x[i]
            second = x[i+1]
            if max == second:
                for j in range(i+2, n):
                    if x[j] != max:
                        second = x[j]
        if i ==1:
            if max < second:
                temp = max
                max = second
                second = temp
        if x[i] > max:  
            second = max
            max = x[i]
        # elif x[i] < max and x[i] != max and x[i] > second:
        #     second = x[i]
        elif x[i] < max and x[i] > second:
            second = x[i]
    return second

if __name__ == "__main__":
    x = [9, 9, 2, 9, 5, 1, 7]
    print(find_secondmax(x))

# 這個寫法太愚蠢了