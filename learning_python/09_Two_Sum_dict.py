# nums = [2,7,11,15], target = 9→ [0,1]
# enumerate(sequence, [start=0])
# 是一個很好用的 Python 工具，它能同時給你"list"的「索引」和「數值
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# (list(enumerate(seasons)))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

def two_sum(nums, target):
    if not isinstance(nums, list) or not isinstance(target, int):
        return None
    for j in nums:
        if not isinstance(j, int):
            return None
    
    my_dict = {}
    for i, element in enumerate(nums):
        x = target - element
        if x in my_dict:
            return [my_dict[x], i]
        my_dict[element] = i
    return None
        
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 26
    print(two_sum(nums, target))
