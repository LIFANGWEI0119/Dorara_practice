def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for i in arr:
        if i > max_val:
            max_val = i
    return max_val


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9]
    print(f"max value = {find_max(data)}")
