def practice_set(x):
    if not isinstance(x, list):
        return None
    
    unique = x
    m = len(x)
    n = len(unique)

    for i in range(0, m):
        for j in range(1, n):
            if x[i] == unique[j]:
                unique.remove(unique[j])
                n = n-1
                j = j-1
    return unique

if __name__ == "__main__":
    x = [9, 9, 2, 9, 5, 1, 7]
    print(practice_set(x))
