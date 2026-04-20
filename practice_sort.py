# def is_string(x):
#     # 在這裡判斷 x 是不是字串
#     y = "abc"
#     if type(x) == type(y):
#      print("It is string")


# x = "hello"
# is_string(x)

# def is_string(x):
#     if type(x) == str:
#         return True

# x = "hello"
# if is_string(x):
#     print("It is string")

# print(type("hello") == str)
# print(type("hello") == "str")

# def is_string(x):
#     return isinstance(x,str)

# print(type([1, 2,3]))

# def sort_number(arr):
#     if isinstance(arr,list):
#         temp = 0
#         for i in range(0,len(arr)):
#             for j in range(i+1,len(arr)):
#                 if arr[i] > arr[j]:
#                     temp = arr[i]
#                     arr[i] = arr[j]
#                     arr[j] = temp
#         return arr
 
# problem = [3, 2, 1]

# ans = sort_number(problem)

# arr = [4, 3, 2]
# i = 1
# j = 2
# arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr):
    error1 = "input must contain  only int or float"
    for x in range(len(arr)):
        if not isinstance(arr[x], (int, float)):
            return error1
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swap = True 
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swap:
            # print(i)
            break
    return arr

problem = [5, 1, 4, 2]
problem2 = [1, 'a', 3, 4]
print(bubble_sort(problem2))

# for i in range(4):
#     print(i)