# 找出只出現一次的數字
# def find_single(seq):
#     if not isinstance(seq, list):
#         return None
#     number_dict = {}
#     for i in seq:
#         if i not in number_dict:
#             number_dict[i] = 1
#         elif i in number_dict:
#             number_dict[i] = number_dict[i] + 1
#     # return number_dict
#     for j in range(0, len(number_dict)):
#         if list(number_dict.values())[j] == 1:
#             return list(number_dict.keys())[j]

def find_single(seq):
    if not isinstance(seq, list):
        return None
    number_dict  = {}
    
    for i in seq:
        number_dict[i] = number_dict.get(i, 0) + 1
    for key, value in number_dict.items():
        if value == 1:
            return key
    return None 
        
if __name__ == "__main__":
    seq = [4, 1, 2, 1, 2]
    print(find_single(seq))

# setdefault()具有取得值及增加項目的功用
# 使用 [] 與 = 增加項目
# 位元運算（Bitwise Operation）
# def single_number(nums):
#     result = 0
#     for num in nums:
#         result ^= num
#     return result