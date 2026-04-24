def find_max(x):
    if not isinstance(x, list) or len(x) == 0:
        return None
    n = len(x)
    max_value = x[0]
    for i in range(0,n):
        if not isinstance(x[i], int):
            return None
        if x[i] > max_value:
            max_value = x[i]
    return max_value

if __name__ == "__main__":
    a = [3, 7, 2, 9, 5, 1]
    print(find_max(a))