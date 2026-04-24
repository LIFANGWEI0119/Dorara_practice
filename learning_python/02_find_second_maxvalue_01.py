#找「第二大的數」
def sort_number(x):
    if not isinstance(x, list):
        return None
    n = len(x)
    for i in range(0, n):
        if not isinstance(x[i], int):
             return None
        for j in range(i+1, n):
                if x[j] < x[i]:
                    # min = x[j]
                    # x[j] = x[i]
                    # x[i] = min
                    x[i], x[j] = x[j], x[i]
    return x
def find_secondmax(x):
     n = len(x)
     x = sort_number(x)
     return x[n-2]
     
if __name__ == "__main__":
     x = [3, 7, 2, 9, 5, 1]
     print(sort_number(x))
     print(find_secondmax(x))
#以上的方法是沒有效率的


